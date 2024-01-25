const fleschTitle = document.getElementById('fleschName')
const fleschHelp = document.getElementById('fleschHelp')

const polarityName = document.getElementById('polarityName')
const polarityHelp = document.getElementById('polarityHelp')

const subjectivityName = document.getElementById('subjectivityName')
const subjectivityHelp = document.getElementById('subjectivityHelp')


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


polarityName.addEventListener('mouseover', () => {
    polarityHelp.classList.remove('hidden')
    polarityHelp.classList.add('opacity-100')
})

polarityName.addEventListener('mouseleave', () => {
    polarityHelp.classList.remove('opacity-100')
    setTimeout(() => {
        polarityHelp.classList.add('hidden');
    }, 100);
})


subjectivityName.addEventListener('mouseover', () => {
    subjectivityHelp.classList.remove('hidden')
    subjectivityHelp.classList.add('opacity-100')
})

subjectivityName.addEventListener('mouseleave', () => {
    subjectivityHelp.classList.remove('opacity-100')
    setTimeout(() => {
        subjectivityHelp.classList.add('hidden');
    }, 100);
})