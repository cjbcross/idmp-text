function initTable() {
    $('#sasTable').bootstrapTable({
        url: '/csv',
        columns: [

                {
                    field: 'target',
                    title: 'Variable',
                    sortable: true,
        filterControl: 'select',
                    align: 'center'
                }, {
                    field: 'match',
                    title: 'Match',
                    sortable: true,
                    editable: true,
                    align: 'center'
                }, {
                    field: 'context',
                    title: 'Context',
                    sortable: true,
                    align: 'left',
                    formatter: matchFormatter
                },{
                    field: 'source',
                    title: 'Source',
                    sortable: true,
                    align: 'center'
                },{
                    field: 'section',
                    title: 'Document Section',
                    sortable: true,
                    align: 'center'
                },{
                    field: 'document',
                    title: 'Document Name',
                    sortable: true,
                    align: 'center'
                }

        ]
    });
}
initTable();


function matchFormatter(data, row, cells) {
    var match = row.match;
    var res = data.replace(match, "<span style='color:#FF3300;'><b>"+match+"</b></span>");
    return res;
}

var $table = $('#sasTable');
$(function () {
    $('#toolbar').find('select').change(function () {
        $table.bootstrapTable('destroy').bootstrapTable({
            exportDataType: $(this).val()
        });
    });
})