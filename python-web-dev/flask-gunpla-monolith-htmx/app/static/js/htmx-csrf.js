document.body.addEventListener('htmx:configRequest', function(evt) {
    evt.detail.headers['X-CSRF-Token'] = document.querySelector('meta[name="csrf-token"]').content;
});

document.body.addEventListener('htmx:afterOnLoad', function(evt) {
    document.getElementById('flash-messages').innerHTML = '';
});
