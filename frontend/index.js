function handleLike() {
    Streamlit.setComponentValue('liked');
    document.getElementById("dislike").style.display = 'none';
    document.getElementById("like").disabled = true;
}

function handleDislike() {
    Streamlit.setComponentValue('disliked');
    document.getElementById("like").style.display = 'none';
    document.getElementById("dislike").disabled = true;
}

function onRender(event) {
    const like = document.getElementById("like");
    like.addEventListener("click", handleLike);
    const dislike = document.getElementById("dislike")
    dislike.addEventListener("click", handleDislike);
    Streamlit.setFrameHeight(document.documentElement.clientHeight);
    key = event["el"]["id"];
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender);
Streamlit.setComponentReady();