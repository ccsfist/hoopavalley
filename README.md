# hoopavalley
Hoopa Valley Tribe sliders

## Embedding the Streamlit display

Each exercise has a `docs/interactiveexercises_<keyword>_2.md` page that embeds the live Streamlit display:

```html
<iframe
  src="https://twowaydisplay.streamlit.app/?game=Coordinate&amp;view=all&amp;present=1&amp;embed=true"
  width="100%"
  style="border: none; height: 90vh;">
</iframe>
```

- Change `game=` to the exercise's game (e.g. `Flood`, `Safe`, `Coordinate`).
- Keep `&embed=true`, which is needed for the app to display inside the iframe.
- Write `&` as `&amp;` in the URL.
- Height is `90vh` (90% of the screen).

## Downloading the streamlit images so that they can be pasted into powerpoint
Run ```python capture_results.py``` in ```docs/download_streamlit_images```
You may need to install this first:
```pip install playwright
playwright install chromium```

The results are saved in streamlit_screenshots

It is not very dynamic, so you need to manually edit the python file to have the right urls and filenames in the DASHBOARDS pairs.
