Title: Pelican on Github Pages 01
Date: 2023-06-08 18:00:00
Category: Python

Github Pages는 퍽 훌륭한 정적 사이트 제공 서비스지만, 그거 하나 쓰자고 달리 써 본 적도 없는 Jekyll을 새로 배우는 건 불합리한 일이었다. 덕분에 쓰다가 말다가를 반복하던 참에, `Pelican`의 존재를 알게 되었다. 파이썬 기반의 정적 사이트 생성기. 그래서 이렇게 작성해 본다.

# Pelican으로 Github Pages 만들기

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