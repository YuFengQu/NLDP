

//#pragma OPENCL EXTENSION cl_khr_fp64: enable


//坡度的表达方式
typedef enum 
{
	DEGREE_SLOPE,		//度数方式
	PERCENT_SLOPE		//百分比方式
}SLOPE_TYPE;

//坡度算法结构体
struct SlopeOption
{
	float dbNsres;				//南北方向分辨率 
	float dbEwres;				//东西方向分辨率 
	SLOPE_TYPE slopeType;		//坡度方式
} ;

//坡向算法结构体
struct AspectOption
{
	int bAngleAsAzimuth;		//是否以正北方向为角度起算方向
};

//山体阴影算法结构体
typedef struct HillshadeOption
{
	float dbNsres;				//南北方向分辨率 
	float dbEwres;				//东西方向分辨率
	float dfzScaleFactor;		//Z方向的缩放因子
	float  dfAzimuth;			//太阳光线的地理方位角
	float  dfAltitude;			//太阳高度
} HillshadeOption;

__kernel void slope_kernel( __global const float *pSrcData,
						 __global float *pDestData,const int nWidth,const int nHeight
						 , struct SlopeOption slopeType)
{
	int nLocalXsize = (int)get_local_size(0);
	int nLocalYsize = (int)get_local_size(1);
	int nLocalX = (int)get_local_id(0);
	int nLocalY = (int)get_local_id(1);
	int nGroupX = get_group_id(0);
	int nGroupY = get_group_id(1);
	int j = nGroupX*nLocalXsize+nLocalX;
	int i = nGroupY*nLocalYsize+nLocalY;

	/*int j = get_global_id(0);
	int i = get_global_id(1);*/

	if (j >= nWidth || i >= nHeight)
		return;


	int nTopTmp = i-1;
	int nBottomTmp = i+1;
	int nLeftTep = j-1;
	int nRightTmp = j+1;

	//处理边界情况
	if (0 == i)
	{
		nTopTmp = i;
	}
	if (0 == j)
	{
		nLeftTep = j;
	}
	if (i == nHeight-1)
	{
		nBottomTmp = i;
	}
	if (j == nWidth-1)
	{
		nRightTmp = j;
	}
	__local float dbRectData[9];
	dbRectData[0] = pSrcData[nTopTmp*nWidth+nLeftTep];
	dbRectData[1] = pSrcData[nTopTmp*nWidth+j];
	dbRectData[2] = pSrcData[nTopTmp*nWidth+nRightTmp];

	dbRectData[3] = pSrcData[i*nWidth+nLeftTep];
	dbRectData[4] = pSrcData[i*nWidth+j];
	dbRectData[5] = pSrcData[i*nWidth+nRightTmp];

	dbRectData[6] = pSrcData[nBottomTmp*nWidth+nLeftTep];
	dbRectData[7] = pSrcData[nBottomTmp*nWidth+j];
	dbRectData[8] = pSrcData[nBottomTmp*nWidth+nRightTmp];

	float dx = ((dbRectData[0] + dbRectData[3]*2 + dbRectData[6]) -
		(dbRectData[2]+ dbRectData[5]*2 + dbRectData[8])) / (slopeType.dbEwres*8);

	float dy =((dbRectData[6] + dbRectData[7]*2 + dbRectData[8]) -
		(dbRectData[0]+ dbRectData[1]*2 + dbRectData[2])) / (slopeType.dbNsres*8);

	float fTmp = (dx *dx + dy * dy);

	//计算坡度
	float radiansToDegrees = 180/M_PI_F;
	float fValue = 0;
	if(slopeType.slopeType == DEGREE_SLOPE)
	{
		fValue = atan(sqrt(fTmp) ) * radiansToDegrees;
	}
	else if (slopeType.slopeType == PERCENT_SLOPE)
		fValue = 100*sqrt(fTmp);

	pDestData[i*nWidth+j] = fValue;

}

__kernel void aspect_kernel( __global const float *pSrcData,
						 __global float *pDestData,const int nWidth,const int nHeight
						 , struct AspectOption aspectType)
{
	int j = get_global_id(0);
	int i = get_global_id(1);

	if (j >= nWidth || i >= nHeight)
		return;


	int nTopTmp = i-1;
	int nBottomTmp = i+1;
	int nLeftTep = j-1;
	int nRightTmp = j+1;

	//处理边界情况
	if (0 == i)
	{
		nTopTmp = i;
	}
	if (0 == j)
	{
		nLeftTep = j;
	}
	if (i == nHeight-1)
	{
		nBottomTmp = i;
	}
	if (j == nWidth-1)
	{
		nRightTmp = j;
	}
	__local float dbRectData[9];
	dbRectData[0] = pSrcData[nTopTmp*nWidth+nLeftTep];
	dbRectData[1] = pSrcData[nTopTmp*nWidth+j];
	dbRectData[2] = pSrcData[nTopTmp*nWidth+nRightTmp];

	dbRectData[3] = pSrcData[i*nWidth+nLeftTep];
	dbRectData[4] = pSrcData[i*nWidth+j];
	dbRectData[5] = pSrcData[i*nWidth+nRightTmp];

	dbRectData[6] = pSrcData[nBottomTmp*nWidth+nLeftTep];
	dbRectData[7] = pSrcData[nBottomTmp*nWidth+j];
	dbRectData[8] = pSrcData[nBottomTmp*nWidth+nRightTmp];

	float dx = (dbRectData[2]+ dbRectData[5]*2 + dbRectData[8])
		-(dbRectData[0] + dbRectData[3]*2 + dbRectData[6]);

	float dy = (dbRectData[6] + dbRectData[7]*2 + dbRectData[8])
	    -(dbRectData[0]+ dbRectData[1]*2 + dbRectData[2]);


	//计算坡向
	float radiansToDegrees = 180/M_PI_F;
	
	float dfAspect = atan2(dy,-dx)*radiansToDegrees;
	
	if (0 == dx && 0 == dy)
	{
		dfAspect = -1;
	}

	else if (aspectType.bAngleAsAzimuth)		//正北向起算
	{
		if (dfAspect > 90)
		{
			dfAspect = 450 - dfAspect;
		}
		else
			dfAspect = 90 - dfAspect;
	}

	else			//正东方向起算
	{
		if (dfAspect < 0)
		{
			dfAspect += 360;
		}
	}

	if (dfAspect == 360)
	{
		dfAspect = 0;
	}

	pDestData[i*nWidth+j] = dfAspect; 

}

__kernel void hillshade_kernel( __global const float *pSrcData,
						 __global float *pDestData,const int nWidth,const int nHeight
						 , struct HillshadeOption hillOption)
{
	int j = get_global_id(0);
	int i = get_global_id(1);

	if (j >= nWidth || i >= nHeight)
		return;


	int nTopTmp = i-1;
	int nBottomTmp = i+1;
	int nLeftTep = j-1;
	int nRightTmp = j+1;

	//处理边界情况
	if (0 == i)
	{
		nTopTmp = i;
	}
	if (0 == j)
	{
		nLeftTep = j;
	}
	if (i == nHeight-1)
	{
		nBottomTmp = i;
	}
	if (j == nWidth-1)
	{
		nRightTmp = j;
	}
	__local float afRectData[9];
	afRectData[0] = pSrcData[nTopTmp*nWidth+nLeftTep];
	afRectData[1] = pSrcData[nTopTmp*nWidth+j];
	afRectData[2] = pSrcData[nTopTmp*nWidth+nRightTmp];

	afRectData[3] = pSrcData[i*nWidth+nLeftTep];
	afRectData[4] = pSrcData[i*nWidth+j];
	afRectData[5] = pSrcData[i*nWidth+nRightTmp];

	afRectData[6] = pSrcData[nBottomTmp*nWidth+nLeftTep];
	afRectData[7] = pSrcData[nBottomTmp*nWidth+j];
	afRectData[8] = pSrcData[nBottomTmp*nWidth+nRightTmp];

	const float degreesToRadians = (M_PI_F / 180);

	float dx = ((afRectData[2]+ afRectData[5]*2 + afRectData[8]) - 
		(afRectData[0] + afRectData[3]*2 + afRectData[6])) / (8 * hillOption.dbEwres);

	float dy = ((afRectData[6] + afRectData[7]*2 + afRectData[8]) -
		(afRectData[0]+ afRectData[1]*2 + afRectData[2])) / (8 * hillOption.dbNsres);

	//计算坡度(弧度)
	float key = sqrt(dx *dx + dy * dy);
	float dfSlope = atan( hillOption.dfzScaleFactor *  key);

	//计算坡向（弧度）
	float dfAspect = 0;
	if (dx != 0)
	{
		dfAspect = atan2(dy,-dx);
		if (dfAspect < 0)
		{
			dfAspect += 2* M_PI_F;
		}
	}

	if (dx == 0)
	{
		if (dy > 0.0f)
		{
			dfAspect = M_PI_F / 2;
		}

		else if (dy < 0.0f)
			dfAspect = M_PI_F + M_PI_F / 2;
	}

	//将太阳高度和太阳光线角度转换为要求的格式
	float dfZenithDeg = hillOption.dfAltitude;

	float dfAzimuthRad = hillOption.dfAzimuth;

	//最后计算山体阴影值
	float dfHillshade = 255 * (cos(dfZenithDeg)*cos(dfSlope) + 
		sin(dfZenithDeg)*sin(dfSlope)*cos(dfAzimuthRad-dfAspect));
	if (dfHillshade < 0)
	{
		dfHillshade = 0;
	}

	if (dfHillshade >= 255)
	{
		dfHillshade = 255;
	}

	pDestData[i*nWidth+j] = (int)(dfHillshade+1/2); 

}