icon: 🦤
Title: Pelican으로 깃허브 페이지 만들기 02
Subtitle: 펠리컨 소개
slug: Pelican on Github Pages 02
Category: python
Series: Github Pages with Pelican
Date: 2024-02-27
Tags: Pelican,Github
Status: published

# 들어가기에 앞서

앞선 글에서는 모든 과정을 `GitHub`에서 진행했습니다. 하지만 이젠 `python`을 써야 하니, 앞으로의 모든 과정은 `vs code`를 사용하는 것을 전제로 해서 진행됩니다. `vs code` 설치 방법은 [여기](https://blog.tykl.me/Pelican-on-Github-Pages-01.html)에 자세히 설명되어 있습니다.

# Pelican

프랑스어로 펜을 뜻하는 ‘calepin’의 아나그램인 `pelican`은 `python` 기반의 정적 사이트 생성기(SSG)입니다. `Jinja2` 템플릿 엔진을 사용하며, 정해진 템플릿과 마크다운/rst 컨텐츠를 바탕으로 HTML 파일을 생성합니다.

## Pelican 설치

`pip install pelican` 명령어 입력으로 설치를 수행합니다.

![Pelican-on-Github-Pages-02_0](/programming/image/Pelican-on-Github-Pages-02_0.png)

## Pelican 시작하기

`pelican-quickstart` 를 입력해 기본적인 `pelican` 페이지를 생성할 수 있습니다. 출력되는 질문에 대답하다 보면 자동적으로 구조에 알맞은 프로젝트를 시작해 줍니다

![Pelican-on-Github-Pages-02_1](/programming/image/Pelican-on-Github-Pages-02_1.png)

`pelican`이 정상 작동하는지 확인하기 위해 `hello-world.md`를 만들고 예시 문서를 작성합니다

![Pelican-on-Github-Pages-02_2](/programming/image/Pelican-on-Github-Pages-02_2.png)

`pelican -l -r`을 입력해 로컬 미리보기 서버를 호출할 수 있습니다.

![Pelican-on-Github-Pages-02_3](/programming/image/Pelican-on-Github-Pages-02_3.png)

![Pelican-on-Github-Pages-02_4](/programming/image/Pelican-on-Github-Pages-02_4.png)

페이지가 정상적으로 적용되었음을 확인할 수 있습니다.

<br/>

기본 템플릿에서 사용할 수 있는 메타데이터는 `Title`, `Date`, `Tag` 등이 있습니다. 분류는 `content`폴더 내에 폴더에 따라 자동으로 분류됩니다.

<br/>

github pages는 main 브랜치, main 브랜치의 docs 폴더, gh-pages 브랜치의 세 가지 배포 옵션이 존재합니다. 이번에는 간편하게 사용할 수 있는 docs 폴더 옵션을 사용합니다. `output` 폴더의 이름을 `docs`로 바꾸고 저장소에 푸시해 줍니다.

![Pelican-on-Github-Pages-02_5](/programming/image/Pelican-on-Github-Pages-02_5.png)

저장소의 Setting > Pages 에서 Source를 Deploy from a branch로, Branch를 main/docs로 지정해 줍니다.

![Pelican-on-Github-Pages-02_6](/programming/image/Pelican-on-Github-Pages-02_6.png)

추후 빌드 시 자동으로 `output` 폴더가 아닌 `docs` 폴더에 작성되도록 `pelicanconf.py`에 다음 줄을 추가해 줍니다.

`OUTPUT_PATH = 'docs/'` 

![Pelican-on-Github-Pages-02_7](/programming/image/Pelican-on-Github-Pages-02_7.png)

github page 주소에 접속해, pelican 페이지가 정상적으로 출력되는 것을 확인합니다

### 참고자료

- [Pelican 홈페이지]([https://getpelican.com/](https://getpelican.com/))

