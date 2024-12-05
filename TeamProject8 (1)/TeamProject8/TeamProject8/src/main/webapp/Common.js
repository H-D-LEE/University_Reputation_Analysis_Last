// 페이지 URL 정의
const mainPageUrl = "./index.html";
const rankPageUrl1 = "./rank.html";
const rankPageUrl2 = "./rankcls.html"
const rankPageUrl3 = "./rankfee.html"
const rankPageUrl4 = "./rankmny.html"
const pagelinkPageUrl = "./pagelink.html";
const standardPageUrl = "./standard.html";

// 컨트롤러 연결 함수 정의
function linkControllersToPages() {
    // 메인 페이지 연결
    const mainPageLink = document.getElementById("mainPageLink");
    mainPageLink.href = mainPageUrl;

    // 랭크 페이지 연결
    const rankPageLink1 = document.getElementById("rankPageLink1");
    rankPageLink1.href = rankPageUrl1;
    const rankPageLink2 = document.getElementById("rankPageLink2");
    rankPageLink2.href = rankPageUrl2;
    const rankPageLink3 = document.getElementById("rankPageLink3");
    rankPageLink3.href = rankPageUrl3;
    const rankPageLink4 = document.getElementById("rankPageLink4");
    rankPageLink4.href = rankPageUrl4;

    // 페이지링크 페이지 연결
    const pagelinkPageLink = document.getElementById("pagelinkPageLink");
    pagelinkPageLink.href = pagelinkPageUrl;

    // 평가기준 페이지 연결
    const standardPageLink = document.getElementById("standardPageLink");
    standardPageLink.href = standardPageUrl;
}

// 페이지 로드 시 컨트롤러 연결 실행
window.onload = linkControllersToPages;
