# Image Optimization Guide

## Why Optimize Images?
Optimizing images improves website speed, enhances user experience, and reduces bandwidth costs.

## Image Formats
1. **JPEG**: Best for photographs and images with many colors.
2. **PNG**: Suitable for images with transparent backgrounds.
3. **WEBP**: Offers superior lossless and lossy compression for images on the web. 

## Optimization Techniques
- **Compression**: Reduce the file size without sacrificing quality.
- **Resizing**: Scale images down to the maximum display size on your website.
- **Lazy Loading**: Load images only when they are visible in the viewport.

## Tools for Optimization
- **ImageMagick**: Command-line tool to convert and optimize images.
- **TinyPNG**: Online tool for compressing PNG and JPEG images.
- **Squoosh**: Web-based tool by Google to compress images efficiently.

## Conversion to WEBP Format
You can convert images to WEBP format using the following script:

```bash
#!/bin/bash

# A simple batch script to convert images to WEBP format

for img in *.png *.jpg; do
  # Get the file name without extension
  filename="${img%.*}"
  # Convert to WEBP format
  cwebp -q 80 "$img" -o "$filename.webp"
done
```

## Conclusion
Optimizing images helps maintain quality while minimizing load times, ensuring your portfolio loads swiftly and efficiently.

---

### Note:
Make sure to have the necessary tools and libraries installed for the conversion process.