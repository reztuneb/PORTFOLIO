# Media Embedding Guide

This site supports high-quality images and videos.

## Add images
1. Place image files in `images/`.
2. Reference them in `index.html` with:

```html
<img src="images/your-file.jpg" alt="Description" />
```

## Add videos
1. Place video files in `videos/`.
2. Reference them in `index.html` with:

```html
<video controls playsinline muted loop>
  <source src="videos/your-file.mp4" type="video/mp4" />
</video>
```

## Best practices
- Use optimized JPEG/PNG/WebP for images.
- Use MP4 (H.264) for widest browser support.
- Keep file names short and lowercase.
- Add `alt` text for accessibility.
