var ghpages = require('gh-pages');

ghpages.publish(
    'public',
    {
        branch: 'gh-pages',
        silent: true,
        repo: 'https://' + process.env.GITHUB_TOKEN + '@github.com/Nautilus-Cyberneering/chinese-ideographs-website.git'
    },
    () => {
        console.log('Deploy Complete!')
    }
)