# Copilot instructions for cat-detection

## Project overview
- This is a static, client-side OpenCV.js demo for detecting cats in uploaded images.
- The main UI and logic live in [index.html](index.html) (inline script, no build tooling).
- OpenCV.js utilities are in [lib/utils.js](lib/utils.js); the Haar cascade model is [cascade.xml](cascade.xml).
- Styling is split by device: desktop in [css/pc.css](css/pc.css), mobile in [css/sp.css](css/sp.css).

## Architecture & data flow
- Page load includes `lib/opencv.js` with `onload="openCvready();"`; `openCvready()` waits for `cv.onRuntimeInitialized` before binding UI events.
- On ready, a `Utils` instance loads [cascade.xml](cascade.xml) into the in-memory FS via `Utils.createFileFromUrl()` (see [lib/utils.js](lib/utils.js)).
- User selects an image → `canvasDraw()` resizes and draws it to `<canvas id="canvas">`.
- User clicks “Detect cat” → `detectCat()` uses `cv.CascadeClassifier` on the canvas image, draws rectangles, updates status text, and releases OpenCV objects with `.delete()`.

## Project-specific conventions
- Keep logic in the inline script block in [index.html](index.html); there is no module bundler or framework.
- Maintain OpenCV.js lifecycle: wait for `cv.onRuntimeInitialized` and use `Utils.createFileFromUrl()` before classifier usage.
- Preserve memory management: when adding OpenCV objects, delete them (`.delete()`) to avoid leaks, as done in `detectCat()`.
- UI messages are routed through `setMessageToStatusArea()` to update `#status_area`.

## Developer workflow notes
- This repo is static assets only (no package.json, build, or tests).
- If you add new assets that must be loaded via XHR (like [cascade.xml](cascade.xml)), ensure they are served from the same origin as the page.

## Key files to reference
- [index.html](index.html): UI structure, event wiring, OpenCV detection flow.
- [lib/utils.js](lib/utils.js): OpenCV loader helpers and file-to-FS utilities.
- [cascade.xml](cascade.xml): Haar cascade model for cat detection.
- [css/pc.css](css/pc.css), [css/sp.css](css/sp.css): desktop/mobile styling rules.
