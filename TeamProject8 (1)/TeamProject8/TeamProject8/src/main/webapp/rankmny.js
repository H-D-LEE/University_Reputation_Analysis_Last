// 페이지 URL 정의
const rankPageUrl1 = "./rank.html";
const rankPageUrl2 = "./rankcls.html";
const rankPageUrl3 = "./rankfee.html";
const rankPageUrl4 = "./rankmny.html";

// 페이지링크 페이지 연결 함수 정의
function linkRankPage() {
    const rankPageLink = document.getElementById("rankPageLink");
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

// 페이지 로드 시 페이지링크 페이지 컨트롤러 연결 실행
window.onload = function() {
    linkRankPage();
    linkRankClsPage();
    linkRankFeePage();
    linkRankMnyPage();
};
