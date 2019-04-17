# 중간 프로젝트

#### 수집하고자 하는 데이터
<p>&nbsp;&nbsp;&nbsp;&nbsp;인스타그램에서 특정 해시태그의 <strong>인기 게시물</strong>에 관한 정보를 수집하고자 한다.</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;인스타그램에서 해시태그를 검색하면 해당 태그가 달린 게시물의 수, 인기 게시물 9개, 최근 게시물, 게시물에 달린 좋아요 수와 댓글 수 등을 얻을 수 있다. 또, 개별 계정 페이지에서는 계정에 있는 게시물의 수, 팔로워 수, 팔로우 수 등에 대한 정보를 얻을 수 있다.
</p>
<br>
#### 활용 가능성
<p>&nbsp;&nbsp;&nbsp;&nbsp;<strong>비즈니스 계정 사용자들에게...</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;인스타그램을 이용하여 마켓팅을 하는 경우를 흔히 볼 수 있다. 인스타그램을 통한 마켓팅은 팔로워 수를 늘리는 것이 중요하고, 팔로워 수를 늘리기 위해서는 해시태그를 잘 활용하는 것이 중요하다고 한다.<br>
&nbsp;&nbsp;&nbsp;&nbsp;인터넷에 검색해보면 인스타 팔로워를 늘리기 위한 해시태그 모음에 관한 포스트들을 많이 볼 수 있다. 많은 사람들이 관심있어 하는 주제임을 알 수 있다. 인기 게시글에 달린 해시태그들을 모아서 인기 해시태그를 알아낼 수 있을 것이다.
</p>
<br>
<p>&nbsp;&nbsp;&nbsp;&nbsp;<strong>일반 계정 사용자들에게...</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;위에서 말했듯이, 인스타그램을 활용한 마케팅에서 중요한 것은 팔로워 수라고 한다. 이로 인해 거짓으로 팔로워 수를 늘려주는 업체 등이 등장했다. 실팔로워 수를 파악하는 것은 소비자가 선택하는 데 도움을 줄 수 있을 것이다.
<br>
&nbsp;&nbsp;&nbsp;&nbsp;"트위터에서 인기 있는 글들이 인스타그램으로 옮겨가고 마지막으로 페이스북으로 넘어간다"는 말을 들은 적이 있다. 이러한 경향이 정말로 존재한다면 팔로워 수를 늘리고 싶어하는 일반 사용자들에게 큰 도움이 될 것이라고 생각한다.(인스타그램에서 정보를 가져오는 것을 해결하면 트위터, 페이스북에서도 인기 게시물에 대한 정보를 수집해야겠다.)
</p>
<br>
#### 환경구축
<p>&nbsp;&nbsp;&nbsp;&nbsp;<strong>R과 phantomjs</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;인스타그램에서 정보가 있는 html 태그를 분석하고 rvest를 이용하여 정보를 가져오려고 했다. 하지만, rvest를 이용하여 가져오는 html코드와 실제 페이지에서 보여지는 html코드가 달랐다.
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;검색을 통해 찾은 이유는 다음과 같다.
<p>&nbsp;&nbsp;&nbsp;&nbsp;인스타그램 페이지는 javascript에 의해 생성되는 부분이 있다. 즉, <U>웹 브라우저가 페이지를 로드한 후에 생성되는 코드가 존재</U>한다. 따라서, 단순히 페이지를 읽어오면 얻을 수 없는 정보가 있다(참고한 사이트: <a href="https://jhb.kr/346?category=645397">https://jhb.kr/346?category=645397</a>). 따라서, phantomjs나 selenium같이 웹 페이지의 상호작용을 자동화하기 위한 도구가 필요하다.
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;수업시간에 phantomjs에 대해 배웠었는데 왜 phantomjs를 사용해야 하는지에 대한 이해가 부족했음을 알게 되었다.
<br>
&nbsp;&nbsp;&nbsp;&nbsp;수업에서 제공된 코드를 이용하여 phantomjs를 통해 페이지를 렌더링한 후의 html코드를 긁어오려고 했다. 하지만 정상적으로 동작하던 코드가 동작하지 않았다. "Invalid flags supplied to RegExp constructor phantomjs://repl-input:1 in a global code"에러가 발생했다. 스크립트에서 정규표현식을 사용하지 않았는데 에러가 나서 해결 방법을 찾지 못했다.
<br>
<br>
<p>&nbsp;&nbsp;&nbsp;&nbsp;<strong>R과 selenium</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;phantomjs 대신에 selenium을 이용해 보았다. selenium과 브라우저 드라이버를 설치하였다(참고한 사이트: <a href="https://hmtb.tistory.com/5">https://hmtb.tistory.com/5</a>).

    library(RSelenium)
    remDr <- remoteDriver(remoteServerAddr="localhost", port=4888L, browserName="firefox")
    remDr$open()
    remDr$navigate("https://www.google.com")


remDr$open()을 실행하자 ""Connecting to remote server"
Undefined error in RCurl call.Error in queryRD(paste0(serverURL, "/session"), "POST", qdata = toJSON(serverOpts)) : "와 같은 에러가 발생했다. 이에 대한 해결책도 찾지 못했다.
</p>
<br>
<p>&nbsp;&nbsp;&nbsp;&nbsp;<strong>Python과 selenium</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;selenium을 검색하면 python 코드가 많이 나와서 python을 이용하기로 했다(참고한 사이트: <a href=http://pythonstudy.xyz/python/article/404-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Selenium-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0">여기</a>).

    from selenium import webdriver
    browser = webdriver.Firefox()
    browser.get("http://google.com")

"Undefined error in RCurl call.Error in queryRD(paste0(serverURL, "/session"), "POST", qdata = toJSON(serverOpts)) :"라는 에러 메시지가 발생하였고 이에 대한 해결책은 <a href="https://stackoverrun.com/ko/q/12260489">여기</a>에서 찾았다. 환경변수 문제였던 것 같다.
</p>
<br>
#### 구현 진행 상황
<p>&nbsp;&nbsp;&nbsp;&nbsp;<strong>특정해시태그의 인기 게시글에 달린 해시태그 수집</strong></p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;#맛스타그램의 총 게시물 수, 인기게시글의 좋아요 수 평균, 인기게시글에 달린 태그들을 수집하였다.(참고한 사이트: <a href="https://seongjaemoon.github.io/python/2018/05/16/python-course6.html">https://seongjaemoon.github.io/python/2018/05/16/python-course6.html</a>)
</p>
<p>&nbsp;&nbsp;&nbsp;&nbsp;댓글 수, 개별 계정 페이지에서 정보 가져오기, 코드 자동 실행, 트위터나 페이스북에서도 정보 가져오기 등을 더 진행해야 한다.
</p>
