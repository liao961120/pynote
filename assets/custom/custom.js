// Put your custom javascript here

document.addEventListener('DOMContentLoaded', () =>{
    // get chapter urls from sidebar
    var li = document.querySelector('.c-sidebar__chapters').querySelectorAll(':nth-child(n+5)');
    var ch_urls = []; 
    for (i=0; i<li.length; ++i) {
        if (li[i].querySelector('a')) 
            ch_urls.push(li[i].querySelector('a').href);
    }

    // modify css property: counter-reset 
    for (i=0; i<ch_urls.length; ++i) {
        if (ch_urls[i] == document.URL) {
            document.querySelector('body').style = `counter-reset: h1 ${i}`
            break
        };
    }
});

