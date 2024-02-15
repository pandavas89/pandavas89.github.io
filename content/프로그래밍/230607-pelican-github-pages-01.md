Title: Pelican on Github Pages 01
Subtitle: Pelican 소개
Date: 2023-06-07
Tags: Pelican, Github, Github Action

`Github Pages`는 퍽 훌륭한 정적 사이트 제공 서비스지만, 그거 하나 쓰자고 달리 써 본 적도 없는 `Jekyll`을 새로 배우는 건 불합리한 일이었다. 덕분에 쓰다가 말다가를 반복하던 참에, `python` 기반 정적 사이트 생성기인 `Pelican`의 존재를 알게 되었습니다. `pelican`으로 정적 사이트를 생성하는 방법을 알아보겠습니다.

1. Pelican을 먼저 설치한다  
  `pip install pelican`
  

2. Pelican 폴더를 생성한다  
  `pelican-quickstart`  
  대화형 프로세스를 끝내면 폴더가 자동으로 생성된다.


3. 예제 포스트를 생성한다  
  Title: Pelican New Post Test  
  Date: 2023-06-08 13:00:00  
  Category: Daily  
  내용을 작성한다


4. 빌드를 수행한다  
  `pelican content`를 입력해서 `content` 폴더 내의 내용을 정적 사이트로 빌드한다.


5. `output/index.html` 에서 빌드 결과를 확인한다.

# 정적 사이트 Github Pages 배포하기
생성된 정적 사이트를 Github Pages로 배포하기 위해서는 기본적인 Github Pages 설정이 필요하다.  
1. 리포지토리 이름을 `{계정명}.github.io`로 바꿔준다.  
2. `gh_pages` 브랜치를 새롭게 만들어 준다. 해당 브랜치는 이후 소스 코드와 빌드 결과 배포를 동시에 진행할 때, 배포 브랜치로 활용된다.  
3. `Settings > Pages` 내의 `Build and Deploy` 항목에서 `Source`를 `Deploy from a branch`로, `Branch`를 `gh_pages/root`로 설정한다.  
4. `.nojekyll` 파일을 로컬 리포지토리의 `output`에 추가한다.  
5. `Settings > Pages` 내의 `Custom Domain`을 설정하고 `Enforce HTTPS`를 체크해 둔 경우, `pelicanconf.py` 내의 `SITEURL`역시 HTTPS로 설정해줘야 정상적으로 테마를 적용시킬 수 있다.  
6. `output` 폴더 내의 모든 파일을 리포지토리의 `gh_pages` 브랜치에 업로드하면 `{계정명}.github.io`에서 배포된 정적 페이지를 확인할 수 있다.  

`.nojekyll`은 `Jekyll`로 작성된 컨텐츠가 아니라는 것을 지시하는 파일로, `Github Pages`의 기본 배포 방식인 `Jekyll` 빌드를 막는다. 해당 파일이 없으면 리포지토리 업로드를 할 때 마다 `Jekyll` 빌드를 시도하므로 `Github Pages`가 정상적으로 표시되지 않는다. `Source`를 `Github Actions`로 바꾸면 `Jekyll` 빌드를 시도하지 않지만, 대신 `Github Pages`의 경로를 지정할 수 없게 되는 문제점이 있다.

다음으로는 배포 전체를 자동화 할 수 있도록 `Github Action`을 작성해보자