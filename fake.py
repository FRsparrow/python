 #代码目的：确定接受哪些乘客预约出行

#公交车基本参数设定
LENGTH = 34;	#服务区域的长度
WIDTH = 1;	#服务区域的宽度
ting = 0.003333;	#站点停靠时间（小时）
v_bus = 30;		#公交车辆的行驶速度
total_time = LENGTH/v_bus*2.2;	#出行总时间
X = [113.858683, 113.877034, 113.900882, 114.045315, 114.1238, 114.148562];	#各站点的经度
Y = [22.581113, 22.570185, 22.56705, 22.544262, 22.56238, 22.575178]

#导入数据库中的乘客预约数据
#乘客预约数据包括以下7个字段：
#出行类型（1、2、3、4）、出行地点经度、出行地点纬度、出行时间窗下限、出行时间窗上限、下车地点经度、下车地点纬度


#如果没有乘客出行数据，可以采用以下方式进行随机模拟产生
N = 40	#出行乘客总人数
N1 = N*0.1	#第一类出行乘客人数
N2 = N*0.4
N3 = N*0.4
N4 = N*0.1
index = zeros(1, 40)	#产生一个长度为40的全零行向量:[0, 0, ..., 0]
chengke = zeros(40, 9)	#产生一个40X9的全零二维数组

#产生N1个第一种类型的乘客:上、下车经纬度，时间均随机产生
for i in range(N1):
	#产生N1个第一类乘客
	arr = find(index == 0)	#找到index中的所有为0的元素的索引
    index1 = arr(ceil(rand*(length(arr))))	#从arr中随机选取一个元素
    index(1, index1) = 1 	#将index中以index1为索引的元素值设置为1
    chengke(index1, 1) = 1		#乘客中行号索引为index1的第一个元素设置为1，表示第一类出行乘客
    
    x = ceil(5*rand) 	#从1-5之间产生一个随机整数
    chengke(index1, 2) = #从X(x):X(x+1)经度范围中随机产生一个数
    chengke(index1, 3) = #从Y(x):Y(x+1)纬度范围中随机产生一个数字
    chengke(index1, 4) = #从0：total_time 中产生一个随机数
    chengke(index1, 5) = chengke(index1, 4) + 1/12
    
    x = x + ceil((5-x)*rand) 	#从x+1:6之间产生一个随机整数
    chengke(index1, 6) = #在X(x):X(x+1)经度范围产生一个随机数
    chengke(index1, 7) = #从Y(x):Y(x+1)纬度范围中产生一个随机数
    
#产生N2个第二种类型的乘客：上车经纬度从X、Y行向量中任意选取一个；下车经纬度随机产生；上车时间随机产生
for i in range(N2):
	arr = find(index == 0)	#找到index中的所有为0的元素的索引
    index1 = arr(ceil(rand*(length(arr))))	#从arr中随机选取一个元素
    index(1, index1) = 1 	#将index中以index1为索引的元素值设置为1
    chengke(index1, 1) = 2		#乘客中行号索引为index1的第一个元素设置为2，表示第二类出行乘客
    
    x = ceil(5*rand) 	#从1:5之间产生一个随机整数
    chengke(index1, 2) = X(x) 		#产生上车的经度
    chengke(index1, 3) = Y(x)	#产生上车的纬度
    #随机产生上车时间
    chengke(index1, 4) = rand*total_time 	
    chengke(index1, 5) = chengke(index1, 4) + 1/12	
    
    x = x + ceil((5-x)*rand) 	#在x：5之间产生一个随机整数
    chengke(index1, 6) = #在X(x):X(x+1)的经度范围之间产生一个随机数
    chengke(index1, 7) = #从Y(x):Y(x+1)纬度范围中产生一个随机数
    
#产生N3个第三种类型的乘客：上车经纬度随机产生；下车经纬度从X,Y中产生；上车时间随机产生
for i in range(N3):
    arr = find(index == 0)	#找到index中的所有为0的元素的索引
    index1 = arr(ceil(rand*(length(arr))))	#从arr中随机选取一个元素
    index(1, index1) = 1 	#将index中以index1为索引的元素值设置为1
    chengke(index1, 1) = 3		#乘客中行号索引为index1的第一个元素设置为3，表示第三类出行乘客
    
    x = ceil(5*rand) 	#从1:5之间产生一个随机整数
    chengke(index1, 2) = #从X(x):X(x+1)经度范围中随机产生一个数字
    chengke(index1, 3) = #从Y(x):Y(x+1)纬度范围中随机产生一个数字
    chengke(index1, 4) = #从0：total_time 中产生一个随机数
    chengke(index1, 5) = chengke(index1, 4) + 1/12
    
    x = #从x+1:6之间随机选取一个整数
    chengke(index1, 6) = X(x)
    chengke(index1, 7) = Y(x)  
#产生N4个第四种类型的乘客：上、下车经纬度从X,Y中选取产生；上车时间随机产生
for i in range(N4):
    arr = find(index == 0)	#找到index中的所有为0的元素的索引
    index1 = arr(ceil(rand*(length(arr))))	#从arr中随机选取一个元素
    index(1, index1) = 1 	#将index中以index1为索引的元素值设置为1
    chengke(index1, 1) = 4		#乘客中行号索引为index1的第一个元素设置为3，表示第四类出行乘客
    
    x = ceil(5*rand) 	#从1:5之间产生一个随机整数
    chengke(index1, 2) = X(x)
    chengke(index1, 3) = Y(x)
    chengke(index1, 4) = #从0：total_time 中产生一个随机数
    chengke(index1, 5) = cengke(index1, 4) + 1/12
    
    x = #从x+1:6之间随机选取一个整数
    chengke(index1, 6) = X(x)
    chengke(index1, 7) = Y(x)


#遗传算法部分
#遗传算法参数设定
L = N	#N表示预约出行乘客总数
NIND = 200
Pc = 0.7;	#交叉概率
Pm = 0.05;	#变异概率
GGAP = 0.85;	#遗传代沟

#产生初始种群
Chrom = crtbp(NIND, L);		产生一个NIND*L维的二进制数组

#计算适应度
ObjV = zeros(NIND, 1)	#产生NIND X 1的列向量
for i in range(NIND):
	ObjV(i) = 1/Fun(Chrom(i, :))	#计算Chrom的第i列的目标函数值

gen = 0		#当前遗传代数
MAXGEN = 200		#总遗传代数
flag = 0	#判定依据
while gen < MAXGEN:
    TempChrom = Chrom	#记录当前种群
    TempVal = ObjV		#记录当前适应度
    gen = gen + 1
    
    # 以下部分应该都有遗传算法库可以调用
    # 计算适应度值，将各染色体的适应度按照从大到小的顺序排序
    FitnV = ranking(ObjV)
    # 选择适应度高的染色体
    # 染色体交叉过程
    # 染色体编译过程
    # 染色体重组过程
    
    
    #记录当前最优个体
    if gen == 1:
       [val, index] = min(1./ObjV)
       best_chrom = Chrom(index,:)
       best_val = val
       trace = [best_val]
       continue
       
    [val, index] = min(1./ObjV)
     if val < best_val:
         best_val = val
         best_chrom = Chrom(index,:)



def Fun(S, chengke):
	STemp = S;
	ret = 0;
	stop_time = 0.003333;%站点停靠时间（小时）
	v_bus = 30;%公交车辆的行驶速度
	X = [113.858683, 113.877034, 113.900882, 114.045315, 114.1238, 114.148562];	#各站点的经度
	Y = [22.581113, 22.570185, 22.56705, 22.544262, 22.56238, 22.575178]
    
    #最大时间窗格限制
	chengke(:, 8) = chengke(:, 4) - 1/12	#第i个乘客的最大时间窗格下线为chengke(i, 4) - 1/12
	chengke(:, 9) = chengke(:, 5) + 1/12	#第i个乘客的最大时间窗格上限为chengke(i, 5) + 1/12
	
	index = find(S == 1)	#找到向量S中为1的所有索引
	S = chengke(index, :)	#找到chengke行号为index的所有行向量
	if length(S) == 0:
		ret = inf
		return ret
	
	# 产生三个空矩阵
	arr_1 = []
	arr_2 = []
	arr = []
	# arr介绍
	# 1、2：上车经纬度
	# 3、4：上车时间窗
	# 5、6：上车最大容忍时间戳
	# 7、8：乘客的索引/1表示上车，2表示下车
	
	for i = 1:size(S, 1)	#进行S的行数次循环
        	     Stemp = S(i,:)	#Stemp取S的第i行
        	     arr_1 = [Stemp(2) Stemp(3) Stemp(4) Stemp(5) Stemp(8) Stemp(9) i 1]
        	     arr_2 = [Stemp(6) Stemp(7) 0 2 0 2 i 2]
        	     arr = [arr;arr_1;arr_2]		#将arr_1,arr_2 append到arr后面
    	end
	
	arr = sortrows(arr, 1)	#将arr按照第一列从小到大排序
	
	# 求解行驶总长度
	L = 0;#线路总长
    	for i = 1:size(arr, 1)		#进行arr的行数次循环
        	     if i == 1
            		Xtemp = X(1)
            		Ytemp = Y(1)
            		continue
        	    end
        	    L = L + abs(arr(i, 1) - Xtemp) + abs(arr(i, 2) - Ytemp);
        	    Xtemp = arr(i-1, 1);
        	    Ytemp = arr(i-1, 2);
              end
    
    #计算每个人的预计到达时间
    t = zeros(size(arr,1), 1)	#产生一个行数与arr相同的列向量
    for i = 1:size(arr, 1)-1	#i从1取到arr的行数-1
        #计算行程时间
        if i == 1
            Xtemp = X(1);
            Ytemp = Y(1);
            t(1) = 0;
            continue
        end
        Temp = (abs(arr(i, 1) - X) + abs(arr(i, 2) - Y)) / v_bus;	#行程时间
        #如果arr的第i行的第一个元素与i-1行的第1个元素相同 并且 第i行的第二个元素==第i-1行的第二个元素，则返回stop_time;否则返回0
        temp = stop_time*(arr(i, 1)==arr(i-1, 1) && arr(i,2)==arr(i-1, 2));		
        
        #记录时间
        t(i) = Temp + temp;
        #更新Xtemp Ytemp
        Xtemp = arr(i, 1);
        Ytemp = arr(i, 2);
    end
    
    t = cumsum(t);		#表示对于t向量累加求和：   比如t = [1, 2, 3, 4]   cumsum(t) = [1, 3, 6, 10]
    
    #计算公交车辆运营费用
    ret1 = 6*L;
    
    #乘客支付费用
    index1 = find(S(:, 1) == 1);	#寻找到S中第1列中为1的元素的索引
    index2 = find(S(:, 1) == 2);	#寻找到S中第1列中为2的元素的索引
    index3 = find(S(:, 1) == 3); 
    index4 = find(S(:, 1) == 4);	length(index1)表示第一类乘客的数量
    ret2 = 4*length(index1) + 3*(length(index2)+length(index3)) + 2 * (length(index4));
	
    #乘客出行的等车延误时间
    ret3 = 0;
    for i = 1:size(arr, 1)			#进行arr的行数次循环
	if arr(i, 3) == 0 && arr(i, 4) == 2
		continue
	end
	ret3 = ret3 + abs(t(i) - arr(i, 3));
    end
    ret3 = 9 * ret3;
	
	
    #乘客出行额外时间花费
    ret4 = 0;
    count = 0;
    for i = 1:size(arr, 1)	进行arr的行数次循环
	if i == 1
	      ret4 = 0;
	      count = count + 1;
	      continue
	end
    
	if arr(i, 1) == arr(i-1, 1) && arr(i, 2) == arr(i-1, 2)
	      if arr(i, end) == 1
		count = count+ 1;
	      elseif arr(i, end) == 2
		count = count - 1;
	      end
	      continue
	end
    
	if arr(i, end) == 1
	      count = count + 1;
	      elseif arr(i, end) == 2
	      count = count - 1;
	end
                ret4 = ret4 + count * stop_time;	
    end
    ret4 = 9 * ret4;
	
    ret5 = timewin(arr, t);		#timewin函数后面进行编写
	
    n = length(find(STemp==1));
    if n < 5
	ret6 = -20*length(find(STemp==1));
    elseif n < 20
	ret6 = 75*n;
    else
	ret6 = 60*n;
    end
	
    ret = ret1 - ret2 + ret3 + ret4 + ret5 + 80 - ret6;
    return ret


def timewin(arr, t):
    n = size(arr, 1);		#n取arr的行数
    ret5 = 0;

    #惩罚系数
    lamda = 4*60;
    yita = 0.5*60;
    
    for iii = 1:n:		#进行n次循环
    	Ttemp = t(iii, :);
                A = arr(iii, :);
	flag = objtest(A, Ttemp);
	switch flag		#对flag进行swith判断
	      case 1
	            ret5 = ret5 + lamda*abs(A(5)-Ttemp) + yita*(A(3)-A(5));
	        case 2
	            ret5 = ret5 + yita*(A(3)-Ttemp);
	        case 3
	            ret5 = ret5 + 0;
	        case 4
	            ret5 = ret5 + yita*(Ttemp-A(4));
	        case 5
	            ret5 = ret5 + yita*(A(6)-A(4)) + lamda*(Ttemp-A(6));
	    end
    end
    return ret5


def objtest(A, temp):
	if Ttemp < A(5)
	    flag = 1;
	elseif Ttemp < A(3)
	    flag = 2;
	elseif Ttemp < A(4)
	    flag = 3;
	elseif Ttemp < A(6)
	    flag = 4;
	elseif Ttemp >= A(6)
	    flag = 5;
	end
	return flag
	
	
