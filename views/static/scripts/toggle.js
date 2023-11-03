function toggle (element, attribute) {
    /**
     * toggle - a function that toggle element
     * element: HTML element to manipulate
     * attribute: Attribute to toggle
     */
    element.classList.toggle(attribute);
}

function dismissal (element, attribute) {
    /**
     * dismissal - a function that dismiss element
     * element: HTML element to manipulate
     * attribute: Attribute to toggle
     */
    if (element.hasAttribute(attribute)) {
        element.classList.remove(attribute);
    }
}

document.querySelector('#toggler').addEventListener('click', function () {
    toggle(document.querySelector('#sidenav'), 'hidden');
}, false);

document.querySelector('#dismiss').addEventListener('click', function () {
    toggle(document.querySelector('#sidenav'), 'hidden');
}, false);