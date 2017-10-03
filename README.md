md-resume-generator
===

## Markdown resume generator develope under python 3 for tech employers

**這是一個科技工作作 / 阿宅 / 工程師 / 程序員用的 markdown 履歷產生器**

- 乾淨、講重點
- 簡化開發流程，只要修改 css

## template reference

- [麻省理工(MIT)的履歷寫作建議 Five Steps to Writing a Great Resume](https://gecd.mit.edu/jobs-and-internships/resumes-cvs-cover-letters-and-linkedin/resumes)

## 使用方法

右上角先 fork
```
    $ git clone git@github.com:<your github account>/md-resume-generator.git
    $ cd ./md-resume.generator
    $ pip install -r requirement.txt # my virtualenv folder is at /home/webuser/venv
    $ vim ./source/resume.md # edit your resume

    $ vim ./source/style/style.css # edit your own css file

    $ ./run.py generate # generate index.html in ./docs
    $ ./run.py server # make a testing server on port 8080
```

## css ribon

- [Fork me on GitHub – CSS ribbon](https://simonwhitaker.github.io/github-fork-ribbon-css/)
