 #����Ŀ�ģ�ȷ��������Щ�˿�ԤԼ����

#���������������趨
LENGTH = 34;	#��������ĳ���
WIDTH = 1;	#��������Ŀ��
ting = 0.003333;	#վ��ͣ��ʱ�䣨Сʱ��
v_bus = 30;		#������������ʻ�ٶ�
total_time = LENGTH/v_bus*2.2;	#������ʱ��
X = [113.858683, 113.877034, 113.900882, 114.045315, 114.1238, 114.148562];	#��վ��ľ���
Y = [22.581113, 22.570185, 22.56705, 22.544262, 22.56238, 22.575178]

#�������ݿ��еĳ˿�ԤԼ����
#�˿�ԤԼ���ݰ�������7���ֶΣ�
#�������ͣ�1��2��3��4�������еص㾭�ȡ����еص�γ�ȡ�����ʱ�䴰���ޡ�����ʱ�䴰���ޡ��³��ص㾭�ȡ��³��ص�γ��


#���û�г˿ͳ������ݣ����Բ������·�ʽ�������ģ�����
N = 40	#���г˿�������
N1 = N*0.1	#��һ����г˿�����
N2 = N*0.4
N3 = N*0.4
N4 = N*0.1
index = zeros(1, 40)	#����һ������Ϊ40��ȫ��������:[0, 0, ..., 0]
chengke = zeros(40, 9)	#����һ��40X9��ȫ���ά����

#����N1����һ�����͵ĳ˿�:�ϡ��³���γ�ȣ�ʱ����������
for i in range(N1):
	#����N1����һ��˿�
	arr = find(index == 0)	#�ҵ�index�е�����Ϊ0��Ԫ�ص�����
    index1 = arr(ceil(rand*(length(arr))))	#��arr�����ѡȡһ��Ԫ��
    index(1, index1) = 1 	#��index����index1Ϊ������Ԫ��ֵ����Ϊ1
    chengke(index1, 1) = 1		#�˿����к�����Ϊindex1�ĵ�һ��Ԫ������Ϊ1����ʾ��һ����г˿�
    
    x = ceil(5*rand) 	#��1-5֮�����һ���������
    chengke(index1, 2) = #��X(x):X(x+1)���ȷ�Χ���������һ����
    chengke(index1, 3) = #��Y(x):Y(x+1)γ�ȷ�Χ���������һ������
    chengke(index1, 4) = #��0��total_time �в���һ�������
    chengke(index1, 5) = chengke(index1, 4) + 1/12
    
    x = x + ceil((5-x)*rand) 	#��x+1:6֮�����һ���������
    chengke(index1, 6) = #��X(x):X(x+1)���ȷ�Χ����һ�������
    chengke(index1, 7) = #��Y(x):Y(x+1)γ�ȷ�Χ�в���һ�������
    
#����N2���ڶ������͵ĳ˿ͣ��ϳ���γ�ȴ�X��Y������������ѡȡһ�����³���γ������������ϳ�ʱ���������
for i in range(N2):
	arr = find(index == 0)	#�ҵ�index�е�����Ϊ0��Ԫ�ص�����
    index1 = arr(ceil(rand*(length(arr))))	#��arr�����ѡȡһ��Ԫ��
    index(1, index1) = 1 	#��index����index1Ϊ������Ԫ��ֵ����Ϊ1
    chengke(index1, 1) = 2		#�˿����к�����Ϊindex1�ĵ�һ��Ԫ������Ϊ2����ʾ�ڶ�����г˿�
    
    x = ceil(5*rand) 	#��1:5֮�����һ���������
    chengke(index1, 2) = X(x) 		#�����ϳ��ľ���
    chengke(index1, 3) = Y(x)	#�����ϳ���γ��
    #��������ϳ�ʱ��
    chengke(index1, 4) = rand*total_time 	
    chengke(index1, 5) = chengke(index1, 4) + 1/12	
    
    x = x + ceil((5-x)*rand) 	#��x��5֮�����һ���������
    chengke(index1, 6) = #��X(x):X(x+1)�ľ��ȷ�Χ֮�����һ�������
    chengke(index1, 7) = #��Y(x):Y(x+1)γ�ȷ�Χ�в���һ�������
    
#����N3�����������͵ĳ˿ͣ��ϳ���γ������������³���γ�ȴ�X,Y�в������ϳ�ʱ���������
for i in range(N3):
    arr = find(index == 0)	#�ҵ�index�е�����Ϊ0��Ԫ�ص�����
    index1 = arr(ceil(rand*(length(arr))))	#��arr�����ѡȡһ��Ԫ��
    index(1, index1) = 1 	#��index����index1Ϊ������Ԫ��ֵ����Ϊ1
    chengke(index1, 1) = 3		#�˿����к�����Ϊindex1�ĵ�һ��Ԫ������Ϊ3����ʾ��������г˿�
    
    x = ceil(5*rand) 	#��1:5֮�����һ���������
    chengke(index1, 2) = #��X(x):X(x+1)���ȷ�Χ���������һ������
    chengke(index1, 3) = #��Y(x):Y(x+1)γ�ȷ�Χ���������һ������
    chengke(index1, 4) = #��0��total_time �в���һ�������
    chengke(index1, 5) = chengke(index1, 4) + 1/12
    
    x = #��x+1:6֮�����ѡȡһ������
    chengke(index1, 6) = X(x)
    chengke(index1, 7) = Y(x)  
#����N4�����������͵ĳ˿ͣ��ϡ��³���γ�ȴ�X,Y��ѡȡ�������ϳ�ʱ���������
for i in range(N4):
    arr = find(index == 0)	#�ҵ�index�е�����Ϊ0��Ԫ�ص�����
    index1 = arr(ceil(rand*(length(arr))))	#��arr�����ѡȡһ��Ԫ��
    index(1, index1) = 1 	#��index����index1Ϊ������Ԫ��ֵ����Ϊ1
    chengke(index1, 1) = 4		#�˿����к�����Ϊindex1�ĵ�һ��Ԫ������Ϊ3����ʾ��������г˿�
    
    x = ceil(5*rand) 	#��1:5֮�����һ���������
    chengke(index1, 2) = X(x)
    chengke(index1, 3) = Y(x)
    chengke(index1, 4) = #��0��total_time �в���һ�������
    chengke(index1, 5) = cengke(index1, 4) + 1/12
    
    x = #��x+1:6֮�����ѡȡһ������
    chengke(index1, 6) = X(x)
    chengke(index1, 7) = Y(x)


#�Ŵ��㷨����
#�Ŵ��㷨�����趨
L = N	#N��ʾԤԼ���г˿�����
NIND = 200
Pc = 0.7;	#�������
Pm = 0.05;	#�������
GGAP = 0.85;	#�Ŵ�����

#������ʼ��Ⱥ
Chrom = crtbp(NIND, L);		����һ��NIND*Lά�Ķ���������

#������Ӧ��
ObjV = zeros(NIND, 1)	#����NIND X 1��������
for i in range(NIND):
	ObjV(i) = 1/Fun(Chrom(i, :))	#����Chrom�ĵ�i�е�Ŀ�꺯��ֵ

gen = 0		#��ǰ�Ŵ�����
MAXGEN = 200		#���Ŵ�����
flag = 0	#�ж�����
while gen < MAXGEN:
    TempChrom = Chrom	#��¼��ǰ��Ⱥ
    TempVal = ObjV		#��¼��ǰ��Ӧ��
    gen = gen + 1
    
    # ���²���Ӧ�ö����Ŵ��㷨����Ե���
    # ������Ӧ��ֵ������Ⱦɫ�����Ӧ�Ȱ��մӴ�С��˳������
    FitnV = ranking(ObjV)
    # ѡ����Ӧ�ȸߵ�Ⱦɫ��
    # Ⱦɫ�彻�����
    # Ⱦɫ��������
    # Ⱦɫ���������
    
    
    #��¼��ǰ���Ÿ���
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
	stop_time = 0.003333;%վ��ͣ��ʱ�䣨Сʱ��
	v_bus = 30;%������������ʻ�ٶ�
	X = [113.858683, 113.877034, 113.900882, 114.045315, 114.1238, 114.148562];	#��վ��ľ���
	Y = [22.581113, 22.570185, 22.56705, 22.544262, 22.56238, 22.575178]
    
    #���ʱ�䴰������
	chengke(:, 8) = chengke(:, 4) - 1/12	#��i���˿͵����ʱ�䴰������Ϊchengke(i, 4) - 1/12
	chengke(:, 9) = chengke(:, 5) + 1/12	#��i���˿͵����ʱ�䴰������Ϊchengke(i, 5) + 1/12
	
	index = find(S == 1)	#�ҵ�����S��Ϊ1����������
	S = chengke(index, :)	#�ҵ�chengke�к�Ϊindex������������
	if length(S) == 0:
		ret = inf
		return ret
	
	# ���������վ���
	arr_1 = []
	arr_2 = []
	arr = []
	# arr����
	# 1��2���ϳ���γ��
	# 3��4���ϳ�ʱ�䴰
	# 5��6���ϳ��������ʱ���
	# 7��8���˿͵�����/1��ʾ�ϳ���2��ʾ�³�
	
	for i = 1:size(S, 1)	#����S��������ѭ��
        	     Stemp = S(i,:)	#StempȡS�ĵ�i��
        	     arr_1 = [Stemp(2) Stemp(3) Stemp(4) Stemp(5) Stemp(8) Stemp(9) i 1]
        	     arr_2 = [Stemp(6) Stemp(7) 0 2 0 2 i 2]
        	     arr = [arr;arr_1;arr_2]		#��arr_1,arr_2 append��arr����
    	end
	
	arr = sortrows(arr, 1)	#��arr���յ�һ�д�С��������
	
	# �����ʻ�ܳ���
	L = 0;#��·�ܳ�
    	for i = 1:size(arr, 1)		#����arr��������ѭ��
        	     if i == 1
            		Xtemp = X(1)
            		Ytemp = Y(1)
            		continue
        	    end
        	    L = L + abs(arr(i, 1) - Xtemp) + abs(arr(i, 2) - Ytemp);
        	    Xtemp = arr(i-1, 1);
        	    Ytemp = arr(i-1, 2);
              end
    
    #����ÿ���˵�Ԥ�Ƶ���ʱ��
    t = zeros(size(arr,1), 1)	#����һ��������arr��ͬ��������
    for i = 1:size(arr, 1)-1	#i��1ȡ��arr������-1
        #�����г�ʱ��
        if i == 1
            Xtemp = X(1);
            Ytemp = Y(1);
            t(1) = 0;
            continue
        end
        Temp = (abs(arr(i, 1) - X) + abs(arr(i, 2) - Y)) / v_bus;	#�г�ʱ��
        #���arr�ĵ�i�еĵ�һ��Ԫ����i-1�еĵ�1��Ԫ����ͬ ���� ��i�еĵڶ���Ԫ��==��i-1�еĵڶ���Ԫ�أ��򷵻�stop_time;���򷵻�0
        temp = stop_time*(arr(i, 1)==arr(i-1, 1) && arr(i,2)==arr(i-1, 2));		
        
        #��¼ʱ��
        t(i) = Temp + temp;
        #����Xtemp Ytemp
        Xtemp = arr(i, 1);
        Ytemp = arr(i, 2);
    end
    
    t = cumsum(t);		#��ʾ����t�����ۼ���ͣ�   ����t = [1, 2, 3, 4]   cumsum(t) = [1, 3, 6, 10]
    
    #���㹫��������Ӫ����
    ret1 = 6*L;
    
    #�˿�֧������
    index1 = find(S(:, 1) == 1);	#Ѱ�ҵ�S�е�1����Ϊ1��Ԫ�ص�����
    index2 = find(S(:, 1) == 2);	#Ѱ�ҵ�S�е�1����Ϊ2��Ԫ�ص�����
    index3 = find(S(:, 1) == 3); 
    index4 = find(S(:, 1) == 4);	length(index1)��ʾ��һ��˿͵�����
    ret2 = 4*length(index1) + 3*(length(index2)+length(index3)) + 2 * (length(index4));
	
    #�˿ͳ��еĵȳ�����ʱ��
    ret3 = 0;
    for i = 1:size(arr, 1)			#����arr��������ѭ��
	if arr(i, 3) == 0 && arr(i, 4) == 2
		continue
	end
	ret3 = ret3 + abs(t(i) - arr(i, 3));
    end
    ret3 = 9 * ret3;
	
	
    #�˿ͳ��ж���ʱ�仨��
    ret4 = 0;
    count = 0;
    for i = 1:size(arr, 1)	����arr��������ѭ��
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
	
    ret5 = timewin(arr, t);		#timewin����������б�д
	
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
    n = size(arr, 1);		#nȡarr������
    ret5 = 0;

    #�ͷ�ϵ��
    lamda = 4*60;
    yita = 0.5*60;
    
    for iii = 1:n:		#����n��ѭ��
    	Ttemp = t(iii, :);
                A = arr(iii, :);
	flag = objtest(A, Ttemp);
	switch flag		#��flag����swith�ж�
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
	
	
