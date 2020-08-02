function updateStudent(id) {
    window.location.href = "/update/"+id;
}
function deleteStudent(id) {
    if (confirm("真的要删除吗？")){
        window.location.href = "/delete/"+id;
    }
}

