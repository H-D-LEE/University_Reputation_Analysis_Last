// 페이지 URL 정의
const pagelinkPageUrl = "./pagelink.html";

// 페이지링크 페이지 연결 함수 정의
function linkPagelinkPage() {
    const pagelinkPageLink = document.getElementById("pagelinkPageLink");
    pagelinkPageLink.href = pagelinkPageUrl;
}

function goToSchoolHomepage(event) {
    event.preventDefault(); // 기본 동작 방지
    const schoolHomepageUrl = event.currentTarget.getAttribute('href');
    window.location.href = schoolHomepageUrl; // 학교 홈페이지로 이동
}
// 학교 홈페이지로 이동 버튼에 클릭 이벤트 추가
document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".btn-secondary");
    buttons.forEach(button => {
        button.addEventListener("click", goToSchoolHomepage);
    });
});

// SNS 링크 클릭 이벤트 추가
document.addEventListener("DOMContentLoaded", function() {
    const snsLinks = document.querySelectorAll(".text-muted > a");
    snsLinks.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault(); // 기본 동작 방지
            const snsUrl = event.currentTarget.getAttribute('href');
            window.location.href = snsUrl; // 해당 SNS 링크로 이동
        });
    });
});
// 페이지 로드 시 페이지링크 페이지 컨트롤러 연결 실행
window.onload = linkPagelinkPage;
