icon: 🦤
Title: Pelican으로 깃허브 페이지 만들기 01
Subtitle: 깃허브 페이지와 정적 사이트 생성기
slug: Pelican on Github Pages 01
Category: python
Series: Github Pages with Pelican
Date: 2024-02-22
Tags: Github
Published: True

제가 `python`으로 기술블로그를 유지하면서 알게 된 것들을 간단하게 얘기하고자 합니다.

# Github Pages

`Github Pages`는 `Github`에서 제공하는 호스팅 서비스입니다. 계정에 따라 `User`, `Organization`, `Project` 깃허브 페이지를 생성할 수 있습니다. 실제로 많은 프로젝트들이 `Github pages`에서 사이트를 호스팅하고 있습니다. 다음은 몇 가지 예시입니다

- [Yeoman]([https://yeoman.io/](https://yeoman.io/))

- [Jekyll]([https://jekyllrb-ko.github.io/](https://jekyllrb-ko.github.io/))

- [bootstrap]([https://getbootstrap.com/](https://getbootstrap.com/))

# GitHub Pages

`Github Pages` 사용하는 방법을 간단하게 설명해 보겠습니다. 초기에 필요한 몇 가지 설정과 나중에 다루게 될 빌드 배포를 제외하면 `Github Pages` 호스팅은 다른 모든 정적 사이트 호스팅과 다르지 않습니다. 이 설명에서는 `User` 깃허브 페이지를 기준으로 설명합니다.

1. GitHub 로그인

	![Pelican on Github Pages 01_0](images/Pelican on Github Pages 01_0.png)

1. repository 생성: {유저 이름}.github.io로 저장소를 생성합니다.

	![Pelican on Github Pages 01_1](images/Pelican on Github Pages 01_1.png)

	- 이 때, 저장소는 public이 아니어도 상관없습니다.

	- 단, private 저장소로 설정하더라도 github pages 상의 모든 문서는 열람할 수 있게 됩니다.

1. `index.html` 파일을 간단하게 생성해 줍니다


	![Pelican on Github Pages 01_2](images/Pelican on Github Pages 01_2.png)

	
```html
<!DOCTYPE html>
<html>
  <body>
    Hello, world!
  </body>
</html>
```

	![Pelican on Github Pages 01_3](images/Pelican on Github Pages 01_3.png)

1. 저장소 설정의 pages에서 `GitHub Pages` 사용을 설정합니다.

	![Pelican on Github Pages 01_4](images/Pelican on Github Pages 01_4.png)

1. 변경 내역을 저장소에 푸시합니다.

1. https://{유저 이름}.github.io에 접속해 변경내역이 반영된 것을 확인합니다.

	![Pelican on Github Pages 01_5](images/Pelican on Github Pages 01_5.png)

1. 새로운 페이지 `hello.html`을 만들어 주고, 링크를 걸어 보겠습니다.

	
```html
<!DOCTYPE html>
<html>
  <body>
    <a href="index.html">back to index</a>
  </body>
</html>
```

	`index.html`에도 새로 만들어 준 `hello.html`을 향한 링크를 걸어주겠습니다. 

	
```html
<!DOCTYPE html>
<html>
  <body>
    Hello, world!<br>
    <a href="https://dev-pandavas.github.io/hello.html">to hello.html</a>
  </body>
</html>
```

	![Pelican on Github Pages 01_6](images/Pelican on Github Pages 01_6.png)

	![Pelican on Github Pages 01_7](images/Pelican on Github Pages 01_7.png)

	두 문서에서 하이퍼링크 방식이 서로 달랐던 걸 눈치채셨나요? 각각 상대주소와 절대주소를 사용했습니다.

<br/>

여러분의 `GitHub Pages`에는 무엇이든 올릴 수 있습니다. 다만, 모든 보여지는 부분과 내용들을 html과 css, 때로는 javascript를 이용해서 작성해야 할 뿐입니다. 하지만 우리 모두가 알듯이, 그건 너무 불편하겠네요.

![Pelican on Github Pages 01_8](images/Pelican on Github Pages 01_8.png)

블로그를 작성하듯  `GitHub Pages`를 작성할 수는 없는걸까요? 걱정하지 마세요. 그런 우리의 걱정을 달래주기 위해 정적 사이트 생성기가 있습니다.

# 정적 사이트 생성기(SSG; Static Site Generator)

정적 사이트 생성기(이하 SSG)는 특정한 규칙에 따라 작성된 컨텐츠와 템플릿에 바탕해서 HTML 페이지를 만들어주는 도구입니다. 규칙에 맞춰 작성하기만 한다면, `GitHub Pages`에 올려야 할 HTML은 모두 SSG가 대신 만들어줍니다. 그리고 그 중에서도 `GitHub Pages`는 `Jekyll`을 기본 SSG로 제공하고 있습니다.

# Jekyll

`Jekyll`은 `Ruby on Rails` 기반의 SSG입니다. 또한, `GitHub Pages`가 기본적으로 제공하는 SSG이기도 합니다. 그러면, 왜 이 시리즈의 제목은 `Jekyll on GitHub Pages`가 아닌걸까요? 왜 `Jekyll`을 사용하지 않고 다른 라이브러리를 쓰려고 하는걸까요?

## Ruby on Rails 기반

`Jekyll`은 `Ruby on Rails` 프레임워크에 기반한 SSG입니다. 그리고 `Ruby on Rails`는 `Ruby` 언어에 기반한 프레임워크입니다. 국내에서 잘 쓰이지 않는 언어와 프레임워크인 탓에, 기술 블로그 하나 운영하겠다고 Jekyll을 배우는 건 수지타산이 맞지 않습니다. 사이드 프로젝트로 진행하는 경우 우리는 익숙한 언어를 사용해 빠르게 구현하고자 하거나, 새롭고 전도유망한 언어를 배우고 적용해 보고자 합니다. 안타깝게도 `Jekyll`은 어느 쪽에도 해당되지 않습니다.

# python 기반 SSG

그래서, 이미 익숙한 언어를 이용해 기술 블로그를 구현하기 위해 `python` 기반의 SSG들을 `JAMStack`에서 찾아봤습니다. `MkDocs`와 `Sphinx`는 각각 프로젝트 문서 작성과 기술 문서 작성을 위한 SSG이고, `Pelican`이 블로그를 구축하기 위한 SSG로는 가장 인기 있는 도구인 셈입니다. 

![Pelican on Github Pages 01_9](images/Pelican on Github Pages 01_9.png)

<br/>

다음 글에서는 `Pelican`을 설치하고 컨텐츠를 작성해 보겠습니다.

---

[예시 블로그](https://dev-pandavas.github.io/)에서 예제를, [저장소](https://github.io/dev-pandavas/dev-pandavas.github.io)에서 코드를 확인해 보실 수 있습니다.

### 참고자료

[GitHub Pages]([https://pages.github.com/](https://pages.github.com/))

[GitHub Docs - GitHub Pages]([https://docs.github.com/ko/pages](https://docs.github.com/ko/pages))

[CloudFlare - Static Site Generator]([https://www.cloudflare.com/ko-kr/learning/performance/static-site-generator/](https://www.cloudflare.com/ko-kr/learning/performance/static-site-generator/))

[JAMStack]([https://jamstack.org/generators/](https://jamstack.org/generators/))

