# Git

## 기본 명령어

1. Git 저장소 설정

   ```python
   $ git init
   ```

   주의! 반드시 현재 디렉토리에 git 을 사용하고 있는지, (master)표시가 없는지 확인

2. `git add`

   current working dir에서 commit할 목록에 파일들을 담기

   그리고 그 목록은 `index(staging area)`라 함

   ```python
   $ git add <folder/file name>
   	(git add .)
   ```

3. git commit

   현재 소스 코드 상태를 저장하는 것(**스냅샷**을 찍는것과 동일)

   `staging area` (git add로 추가한 파일들이 담기는 곳)에 있는 내용을 이력으로 기록

   ```
   $ git commit -m "MESSAGE(내가 표시할 내용)"
   ```

4. git status

   git의 현재 상태를 확인

   커밋할 목록에 담겨있는지, untracked 인지, 커밋할 내역이 있는지 등 다양한 정보 제공

   ```
   $ git status 
   ```

5. git log

   현재까지 커밋된 모든 이력을 확인

   ```
   $ git log
   ```



## 원격저장소 활용하기

1. remote repository 등록

   원격 저장소를 등록 >> origin의 이름으로 

   최초 한 번만 등록

   ```
   $ git remote add origin <경로>
   ```

   `git remote -v` 로 확인

   ```
   $ git remote -v
   origin  https://github.com/young31/TIL.git (fetch)
   origin  https://github.com/young31/TIL.git (push)
   ```

2. 원격 저장소에 올리기

   origin이라는 원격 저장소의 master branch로 지금까지의 커밋 내역을 올림

   ```
   $ git push origin(저장소이름) master(브랜치이름)
   ```

3. 원격저장소에서 가져오기

   ```
   $ git pull origin master 
   ```

4. 원격 저장소를 로컬에 복사하기

   다운받기를 원하는 폴더에서 git bash열고 실행

   경로는 git에서 clone or download

   ```
   $ git clone <경로 (<< git에서 추출)>
   ```

ref : [backlog.com]





