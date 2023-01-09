// App code-base initialistaion goes here.

// Load app-wide styles. Those will affect
// every component. For Vue-component-specific styles
// see scoped CSS.
require('./app.scss')

const nodeList = document.querySelectorAll(
    'article.observation'
);

[...nodeList].forEach((observation) => {
    if (observation.classList.contains('no-more-link')) {
        return;
    }

    const link = document.createElement('span');
    link.classList.add("observation-hide");

    link.addEventListener('click', () => {
        observation.classList.toggle('open');
    })

    observation.appendChild(link);
});
