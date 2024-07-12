let listElements = document.querySelectorAll(".dropdown__link");

listElements.forEach((listElement) => {
    listElement.addEventListener("click", () => {
        let height = "0";

        let menu = listElement.nextElementSibling;
        menu.style.padding = "0";

        if (menu.clientHeight == "0") {
            listElement.classList.toggle("arrow");
            height = menu.scrollHeight + "px";
            menu.style.padding = "1em";
        }

        menu.style.height = height;
    });
});