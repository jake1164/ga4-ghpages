<div align="center"> 
    <h2 >ga4-ghpages Action</h2>
    <img alt="GA4 Logo" src="./images/analytics-logo.png" />
    <h4>Inject your Google Analytics tracking tag into github pages </h4>
</div>

<hr />

This is a GitHub action for injecting [google analytics 4 tracking](https://support.google.com/analytics/answer/9304153) into a GitHub Pages static site during deployment.

## Usage

This action uses python to inject your Google tag immediately before the </Head> tag. 

### Example workflow

``` yaml
name: Your Workflow
on: 
    release:
        type: [published]
jobs:
    deploy-to-github-pages:
    # Using ubuntu latest
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4

    #######  Build your project  #######
    ### ...
    ### Note the folder holding your final HTML
    ### In this example its release/wwwroot

    - name: Inject GA4 tracking code
      uses: jake1164/ga4-ghpages@v1
      with:
        tracking_id: ${{ secrets.GA4_TRACKING_ID }} # example: G-11XXXXXXXX
        file: release/wwwroot/index.html # your publish_dir to your html code before being published.

    - name: Commit To GithubPages
      uses: peaceiris/actions-gh-pages@v4
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}
        publish_dir: release/wwwroot 
        force_orphan: true
```

### Inputs
| Input                 | Description                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|
| `tracking_id`         | Your Google tracking ID - ie  G-11XXXXXXXX                                                                          |
| `file`                | Name and Path of the index.html file (or any file with a </head>) where you want your google tag injected           |

### Outputs

No direct output apart from file with GA4 tag injected just before the </head> tag.


