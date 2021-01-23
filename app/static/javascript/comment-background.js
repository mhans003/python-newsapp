//Alternate blue/yellow background color for each comment.

const headingContainers = document.querySelectorAll(".comment-heading-container");

headingContainers.forEach((element, index) => {
    if(index % 2) {
        element.classList.add("comment-heading-container-blue");
    } else {
        element.classList.add("comment-heading-container-yellow");
    }
});

