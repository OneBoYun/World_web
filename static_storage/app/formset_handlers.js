
KindEditor.ready(function(K) {
    K.create('textarea[name="new_content"]', {
        width : "800px",
        height : "500px",
        uploadJson: '/admin/uploads/kindeditor',
    });
});