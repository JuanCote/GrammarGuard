const fleschTitle = document.getElementById('fleschName')
const fleschHelp = document.getElementById('fleschHelp')


document.addEventListener('DOMContentLoaded', function () {
    const highlightedWords = document.querySelectorAll('.highlighted-word');

    highlightedWords.forEach(function (word) {
        word.addEventListener('mouseover', function () {
            const correctWord = word.dataset.correctWord;
            const range = document.createRange();
            range.selectNodeContents(word);

            const rect = range.getBoundingClientRect();
            showTooltip(rect.x - 10, rect.y - 50, correctWord);
        });

        word.addEventListener('mouseout', function () {
            hideTooltip();
        });
    });
});

function showTooltip(x, y, text) {
    const tooltip = document.getElementById('tooltip');
    tooltip.innerHTML = text;
    tooltip.style.left = x + 'px';
    tooltip.style.top = y + 'px';
    tooltip.classList.remove('hidden');
    tooltip.classList.add('opacity-100');
}

function hideTooltip() {
    const tooltip = document.getElementById('tooltip');
    tooltip.classList.remove('opacity-100');
    setTimeout(() => {
        tooltip.classList.add('hidden');
    }, 100);
}


fleschTitle.addEventListener('mouseover', () => {
    fleschHelp.classList.remove('hidden')
    fleschHelp.classList.add('opacity-100')
})

fleschTitle.addEventListener('mouseleave', () => {
    fleschHelp.classList.remove('opacity-100')
    setTimeout(() => {
        fleschHelp.classList.add('hidden');
    }, 100);
})