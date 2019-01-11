def check(connections, i, j,m_x,m_y):
    if j==len(connections[0]) :
        j=0;
    if j==-1:
        j=len(connections[0])-1
    if not (0 <= i < len(connections)) or not (0 <= j < len(connections[0])):
        return 0

    if connections[i][j] != 1:
        return 0
   # if (ii==m_x and jj==m_y):
   #     return -400
    result = 1
    connections[i][j] = 0
    
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            if i != ii or j != jj:
                if i == ii or j == jj:
                    result += check(connections, ii, jj,m_x,m_y)
    #print(result)
    return result


def maximum(connections,m_x,m_y):
    result = 0
    check(connections, m_x, m_y,m_x,m_y)
    for i in range(len(connections)):
        for j in range(len(connections[0])):
            result = max(result, check(connections, i, j,m_x,m_y))           
    return result

while EOFError:
    s=input()
    if s is None:
        break
        exit(0)
    if len(s.split(' '))==2 :
        m , n=s.split(' ')
        try:
            graph = []
            for _ in range(int(m)):
                row =[c for c in input()]        
                graph.append(row)
            m_x,m_y=input().split(' ')
            m_x=int(m_x)
            m_y=int(m_y)
            land=graph[m_x][m_y]
            for iii in range(int(m)):
                for jjj in range(int(n)):
                    if graph[iii][jjj]==land:
                        graph[iii][jjj]=1
                    else :
                        graph[iii][jjj]=0
            print(maximum(graph,m_x,m_y))
            z=input()
           # if z!='' or z:
            #    break
        except Exception :
            break
    else :
        break
exit(0)
