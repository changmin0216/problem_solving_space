from collections import deque

def find_route(sy, sx, ty, tx):
    q = deque()
    q.append((sy, sx, []))

    visited = [[False]*n for _ in range(n)]
    visited[sy][sx] = True

    while q:
        ey, ex, r= q.popleft()
        if ey==ty and ex==tx:
            return r[:-1]

        for dy, dx in ((-1,0),(1,0),(0,-1),(0,1)):
            ny, nx = ey + dy, ex + dx

            if 0<=ny<n and 0<=nx<n:
                if graph[ny][nx] == 0 and visited[ny][nx]==False :
                    visited[ny][nx] = (ey, ex)
                    q.append((ny, nx, r+[(ny, nx)]))
    return -1


    # 상, 우상, 우, 우하, 하, 좌하, 좌, 좌상
    # 0, 1, 2, 3, 4, 5, 6, 7
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
def mark_line(v, ci, cj, d):
    while 0<=ci<n and 0<=cj<n:
        v[ci][cj] = 2
        ci, cj = ci + dy[d], cj + dx[d]

def mark_safe(v, si, sj, dr, org_dr):
    # [1] 직선방향 표시
    ci, cj = si+dy[dr], sj+dx[dr]
    mark_line(v, ci, cj, dr)

    # [2] 바라보는 방향으로 한줄씩 표시
    ci, cj = si + dy[org_dr], sj + dx[org_dr]
    while 0<=ci<n and 0<=cj<n:
        mark_line(v, ci, cj, dr)
        ci, cj = ci + dy[org_dr], cj + dx[org_dr]

def make_stone(warr, mi, mj, d):
    v = [[0]*n for _ in range(n)]
    cnt = 0

    # [1] d 방향으로 >0 만날때까지 1표, 이후 좌표 2 표시
    ni, nj = mi+dy[d], mj+dx[d]
    while 0<=ni<n and 0<=nj<n:
        v[ni][nj] = 1
        if warr[ni][nj] > 0: ##전사가 있으면
            cnt+=warr[ni][nj]
            ni, nj = ni + dy[d], nj + dx[d]
            mark_line(v, ni, nj, d)
            break
        ni, nj = ni + dy[d], nj + dx[d]

    # [2] d-1, d+1 방향으로 동일처리, 대각선 원점 잡고 d 방향
    for org_d in ((d-1)%8, (d+1)%8):
        si, sj = mi + dy[org_d], mj + dx[org_d]
        while 0<=si<n and 0<=sj<n:
            if v[si][sj] == 0 and warr[si][sj] > 0:
                v[si][sj] = 1
                cnt+=warr[si][sj]
                mark_safe(v, si, sj, d, org_d)
                break

            ci, cj = si, sj # 첫 위치가 전사 아니면 계속 아래로 진행
            while 0<=ci<n and 0<=cj<n:
                if v[ci][cj] == 0:
                    v[ci][cj] = 1
                    if warr[ci][cj] > 0: # 전사가 있으면
                        cnt+=warr[ci][cj]
                        mark_safe(v,ci,cj,d,org_d)
                        break
                else: # 이미 방문했으면
                    break
                ci, cj = ci + dy[d], cj + dx[d],

            si, sj = si + dy[org_d], sj + dx[org_d]
    return v, cnt

def move_warr(v, mi, mj):
    # (상,하,좌,우), (좌,우,상,하) (!=1이면 움직일 수 있다)
    move, attack = 0, 0

    for dirs in (((-1,0),(1,0),(0,-1),(0,1)), ((0,-1),(0,1),(-1,0),(1,0))):
        for idx in range(len(warriors)-1, -1, -1):
            ci, cj = warriors[idx]
            if v[ci][cj]==1:
                continue

            dist = abs(mi-ci)+abs(mj-cj)

            for di, dj in dirs:
                ni, nj = ci+di, cj+dj
                # 범위 내 메두사 시야 아니고 현재보다 줄어드는 방법
                if 0<=ni<n and 0<=nj<n and v[ni][nj]!=1 and dist>abs(mi-ni)+abs(mj-nj):
                    if (ni, nj)==(mi,mj):
                        attack+=1
                        warriors.pop(idx)
                    else:
                        warriors[idx] = [ni, nj]
                    move+=1
                    break
    return move, attack

####################################

n, m = map(int, input().split())
si, sj, ei, ej = map(int, input().split())

warriors = []
tmp = list(map(int, input().split()))
for i in range(0, len(tmp), 2):
    warriors.append([tmp[i], tmp[i+1]])

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# [0] bfs로 메두사의 최단 경로를 저장
route = find_route(si, sj, ei, ej)
if route == -1: ## 경로가 없으면
    print(-1)
else:
    for mi, mj in route:
        mv_cnt, attack_cnt = 0, 0

        # [1] 메두사의 이동 : 지정된 최단거리로 이동(전사 만나면 죽여)
        for i in range(len(warriors)-1, -1, -1): ## 삭제시 역순으로
            if warriors[i] == [mi, mj]:
                warriors.pop(i)

        # [2] 메두사의 시선 : 상하좌우 방향 중 가장 전사를 많이 보는 방향
        warr = [[0]*n for _ in range(n)]
        for ti, tj in warriors:
            warr[ti][tj]+=1

        mx_stone = -1
        v = []
        for d in (0,4,6,2):
            tv, tstone = make_stone(warr, mi, mj, d)
            if mx_stone < tstone:
                mx_stone = tstone
                v = tv

        # [3] 전사의 이동(한 칸씩 두번) : 메두사가 있는 경우 공격
        mv_cnt, attack_cnt = move_warr(v, mi, mj)

        print(mv_cnt, mx_stone, attack_cnt)
    print(0)