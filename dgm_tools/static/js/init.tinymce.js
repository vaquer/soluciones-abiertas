tinymce.init({
    selector:'textarea#id_text',
    width: 610,
    schema : 'html5',
    fontsize_formats: "8px 10px 12px 14px 18px 24px 36px",
    force_br_newlines: false,
    convert_newlines_to_brs : false,
    plugins: "code",
    toolbar: "undo, redo, formatselect, bold, italic, alignleft, aligncenter, alignright, alignjustify, alignnone, outdent, indent, blockquote, removeformat, code",
});