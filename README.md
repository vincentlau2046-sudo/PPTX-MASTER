# PPT Master

AI-driven multi-format SVG content generation system for professional presentations.

## Version History

### v1.1.1 (2026-04-11) - Huawei Template Integration

**Added:**
- Huawei Technologies brand template (`华为技术`)
- New `enterprise` quick lookup category in template index
- Template count updated to 21

**Changed:**
- `layouts_index.json`: Added Huawei template to brand category and technology/enterprise lookups
- `README.md`: Updated template index with Huawei template details

**Use Case:**
- Enterprise reports, solution showcases, annual reports, B2B client communication
- Minimalist tech style with Huawei red accents and professional gray tones

---

### v1.1.0 (2026-04-09) - Source File Handling Update

**Changed:**
- Source files are now **copied** (not moved) to `sources/` directory by default
- Original files are preserved at their source location
- Use `--move` flag if you want to move files instead of copying

**Previous behavior (v1.0.x):**
- Source files were moved to `sources/`, removing them from original location

**Rationale:**
- Safer default behavior - originals are preserved
- Users can still opt-in to move behavior with `--move` flag
- Reduces risk of accidental data loss

---

### v1.0.0 (2026-04-08) - Initial Release

**Features:**
- Multi-format input support (PDF, DOCX, EPUB, HTML, URL, Markdown)
- Professional SVG generation with design system
- Template-based and free-design modes
- Eight Confirmations design specification
- PPTX export with speaker notes
- Icon embedding and image processing

---

## Usage

```bash
# Initialize project
python3 scripts/project_manager.py init <project_name> --format ppt169

# Import source files (default: copy, preserve originals)
python3 scripts/project_manager.py import-sources <project_path> <source_files...>

# Import source files (move mode - remove originals)
python3 scripts/project_manager.py import-sources <project_path> <source_files...> --move

# Generate PPTX
python3 scripts/svg_to_pptx.py <project_path> -s final
```

## License

MIT
