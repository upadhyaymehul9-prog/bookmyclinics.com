const CACHE_NAME = 'bookmyclinic-v4';
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json'
];
// Install — cache static assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(STATIC_ASSETS))
  );
  self.skipWaiting();
});
// Activate — clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});
// Fetch — network first, fallback to cache for static; 
// For /app routes (GAS proxy), always network
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  // Always fetch app routes from network
  if (url.pathname.startsWith('/app')) {
    event.respondWith(fetch(event.request));
    return;
  }
  // Static assets: network first, then cache
  event.respondWith(
    fetch(event.request).then(response => {
      if (response && response.status === 200) {
        const clone = response.clone();
        caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
      }
      return response;
    }).catch(() => {
      return caches.match(event.request).then(cached => {
        return cached || caches.match('/index.html');
      });
    })
  );
});
