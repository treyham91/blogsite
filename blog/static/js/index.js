document.onload = function() {
    let likeLink = document.getElementById("like-link");
    likeLink.addEventListener("click", function() {
        document.body.style.zIndex = '-1';
    })
}