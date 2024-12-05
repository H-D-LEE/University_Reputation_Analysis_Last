// 파이썬 연결

// const { response } = require("../../../../../../myapp/app");


// 페이지 URL 정의
const standardPageUrl = "./standard.html";
const rankPageUrl1 = "./rank.html";
const rankPageUrl2 = "./rankcls.html";
const rankPageUrl3 = "./rankfee.html";
const rankPageUrl4 = "./rankmny.html";

// 평가기준 페이지 연결 함수 정의
function linkStandardPage() {
    const standardPageLink = document.getElementById("standardPageLink");
    standardPageLink.href = standardPageUrl;
}

// 페이지링크 페이지 연결 함수 정의
function linkRankPage() {
    const rankPageLink = document.getElementById("rankPageLink1");
    rankPageLink.href = rankPageUrl1;
}

function linkRankClsPage() {
    const rankClsPageLink = document.getElementById("rankPageLink2");
    rankClsPageLink.href = rankPageUrl2;
}

function linkRankFeePage() {
    const rankFeePageLink = document.getElementById("rankPageLink3");
    rankFeePageLink.href = rankPageUrl3;
}

function linkRankMnyPage() {
    const rankMnyPageLink = document.getElementById("rankPageLink4");
    rankMnyPageLink.href = rankPageUrl4;
}

//스크랩된 데이터 저장용 전역 변수
let fetchedData = [];

function selectData() {
    console.log("검색이 실행됩니다.");
    var key = document.getElementById("searchInput").value;
    var searchResults = document.getElementById("searchResults");
    searchResults.innerHTML = "";
    fetch("http://localhost:7070/search?keyword=" + key)
    .then((res) => res.json())
    .then((data) => {
        // data를 응답 받은 후의 로직
        console.log(data);
        fetchedData=data; //data를 전역 변수에 저장 //
        data.forEach((item) => {
            var div = document.createElement("div");
            div.textContent = item['review_title'];
            searchResults.appendChild(div);
        })
    });
}

function analyze() {
    console.log("분석 시작.");
    fetch("http://localhost:5050/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(fetchedData)
    })
    .then((res) => res.json())
    .then((results) => {
        const analysisDiv = document.getElementById("analysisResults");
        analysisDiv.innerHTML = "";
        Object.values(results).forEach((result, index) => {
            const div = document.createElement("div");
            div.innerText = `${index+1}
                                제목: ${fetchedData[index]['review_title']} \n
                                내용: ${fetchedData[index]['review_content']} \n
                                감성 분석 결과: ${Object.values(result)[0]}`;
            analysisDiv.appendChild(div);
        });
    })
    .catch((error) => {
        console.error("Error analyzing sentiment:", error);
    })
}

function craw(key) {
    console.log("크롤링 실행");
    fetch('http://localhost:5000/searchPost', {
        method: 'POST',
        body: JSON.stringify({
            keyword: key
        })
    }).then(console.log("크롤링 완료"))
};

function search() {
    var key = document.getElementById("searchInput").value;
    craw(key);
}

// 캐시를 지우는 함수
// function clearCache() {
//     if (window.location.href.indexOf("?") > -1) {
//         // 현재 URL에 이미 쿼리 문자열이 있는 경우, 뒤에 랜덤 숫자를 붙여 캐시를 피하도록 함
//         window.location.href += "&_=" + new Date().getTime();
//     } else {
//         // 현재 URL에 쿼리 문자열이 없는 경우, 뒤에 랜덤 숫자를 붙여 캐시를 피하도록 함
//         window.location.href += "?_=" + new Date().getTime();
//     }
// }

// // 페이지 로드 시 캐시를 지우는 함수 호출
// window.onload = function() {
//     clearCache();
// };

// 보러가기 버튼 클릭 이벤트 핸들러 추가
document.addEventListener("DOMContentLoaded", function() {
    const rankPageLink = document.getElementById("rankPageLink1");
    const rankClsPageLink = document.getElementById("rankPageLink2");
    const rankFeePageLink = document.getElementById("rankPageLink3");
    const rankMnyPageLink = document.getElementById("rankPageLink4");

    rankPageLink.addEventListener("click", function(event) {
        event.preventDefault(); // 기본 동작 방지
        window.location.href = rankPageUrl1;
    });

    rankClsPageLink.addEventListener("click", function(event) {
        event.preventDefault(); // 기본 동작 방지
        window.location.href = rankPageUrl2;
    });

    rankFeePageLink.addEventListener("click", function(event) {
        event.preventDefault(); // 기본 동작 방지
        window.location.href = rankPageUrl3;
    });

    rankMnyPageLink.addEventListener("click", function(event) {
        event.preventDefault(); // 기본 동작 방지
        window.location.href = rankPageUrl4;
    });
});
// 페이지 로드 시 평가기준 페이지 컨트롤러 연결 실행
window.onload = linkStandardPage;
