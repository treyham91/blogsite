window.onload = function() {
    let postFormContainer = document.getElementById("post-form-container");
    let postForm = document.getElementById("post-form");
    let loader = document.createElement("div");
    loader.setAttribute("class", "loader");
    loader.style.border  = '16px solid #f3f3f3';
    loader.style.borderRadius = '50%';
    loader.style.borderTop = '16px solid #3498db';
    loader.style.width = '120px';
    loader.style.height = '120px';
    loader.style.animation = 'spin 2s linear infinite';

    while (postForm === undefined) {
        postFormContainer.appendChild(loader);
    }
    // Removes the default Title value set by the model
    document.getElementById("id_title").setAttribute("value", "");
    return postForm;
}