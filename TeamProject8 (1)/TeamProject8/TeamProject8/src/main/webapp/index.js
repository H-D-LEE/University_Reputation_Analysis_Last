// 페이지 URL 정의
const mainPageUrl = "./index.html";

// 메인 페이지 연결 함수 정의
function linkMainPage() {
    const mainPageLink = document.getElementById("mainPageLink");
    mainPageLink.href = mainPageUrl;
}

// 페이지 로드 시 메인 페이지 컨트롤러 연결 실행
window.onload = linkMainPage;
