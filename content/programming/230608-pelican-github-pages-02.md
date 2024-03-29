Title: Pelican on Github Pages 02
Subtitle: Github Action 기반 배포 자동화하기
Date: 2023-06-08 18:00:00
Tags: Pelican, Github, Github Action
Series: Github_Pages_with_Pelican
status: hidden

[앞선 글](/pelican-on-github-pages-01)에서, `Pelican`으로 정적 사이트를 생성하고 배포하는 방법을 알아보았습니다. 이제, `Pelican` 프로젝트를 푸시하면 자동으로 `Github Pages`가 업데이트 되도록 해 보겠습니다.

# Github Action 기반 배포 자동화하기
1. 리포지토리 루트 폴더에 `.github/workflows`를 생성해 줍니다.
2. `pelican_github_pages_deloy.yml` 파일을 생성하고 다음과 같이 입력합니다
  ```
  name: build and deploy pelican outputs
  
  permissions:
    contents: write
  
  on:
    push:
      branches:["main"]
  
  jobs:
    build:
      runs-on: ubuntu-latest
  
      steps:
        - uses: actions/checkout@v3
  
        - run: pip install pelican markdown
        - run: pelican content
        - run: echo "[Custom URL]" >> output/CNAME
        - run: echo "" >> output/.nojekyll
        - run: git config user.name github-actions
        - run: git config user.email github-actions@github.com
        - run: git --work-tree output add --all
        - run git commit -m "Automatic deployment by github-actions"
        - run: git push origin HEAD:gh_pages --force
  ```

3. 로컬 리포지토리(`Pelican` 프로젝트) 내의 파일들을 `Github Pages`의 `main` 브랜치에 푸시합니다.
4. `Github Action`을 설정해 주었기 때문에, Push의 결과로 Github Action이 작동합니다. 리포지토리의 Action 탭에서 확인할 수 있습니다.

이로써 프로젝트 푸시에 따라 자동적으로 Github Pages가 업데이트되도록 설정했습니다다.