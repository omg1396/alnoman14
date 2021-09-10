odoo.define('base_list_sequence.ListRenderer', function(require) {
"use strict";

var ListRenderer = require('web.ListRenderer');

ListRenderer.include({
    /**
     * Render all rows. This method should only called when the view is not
     * grouped.
     *
     * @private
     * @returns {jQueryElement[]} a list of <tr>
     */
    _renderRows: function () {
        var rows = this._super.apply(this, arguments);
        this._addSequence(rows);
        return rows;
    },
    _createSeqCell: function(seq){
        var tdClassName = 'o_list_number';
        var $td = $('<td>', { class: tdClassName, tabindex: -1 }).html(seq);
        return $td;
    },
    _addSequence: function(rows){
        var k = 0;
        for(var i=0; i < rows.length; ++i) {
            var j = i + this.state.offset + 1 - k;
            if (rows[i].hasClass('o_is_line_note') || rows[i].hasClass('o_is_line_section')){
                j = '';
                k += 1;
            }
            var $td = this._createSeqCell(j);
            rows[i].prepend($td);
        }
    },
    _renderHeader: function () {
        var $thead = this._super.apply(this, arguments);
        $thead.find('tr').prepend($('<th class="o_list_seq_th">#.</th>'));
        return $thead;
    },
//    _renderEmptyRow: function(){
//        var $tr = this._super.apply(this, arguments);
//        if (!this.editable){
//            $tr.prepend($('<td class="oe_read_only" />'));
//        }
//        return $tr;
//    },
//    _renderFooter: function(){
//        var $tfoot = this._super.apply(this, arguments);
//        if (!this.editable){
//            $tfoot.find('tr').prepend($('<td class="oe_read_only" />'));
//        }
//        return $tfoot;
//    },
    _renderFooter: function (isGrouped) {
    	var $footer = this._super(isGrouped);
    	$footer.find("tr").prepend($('<td>'));
    	return $footer;
    },
    _renderGroupRow: function (group, groupLevel) {
        var $row =  this._super(group, groupLevel);
        if (this.mode !== 'edit' || this.hasSelectors){
        	$row.find("th.o_group_name").after($('<td>'));
        }
        return $row;
    },
    _renderGroups: function (data, groupLevel) {
    	var self = this;
    	var _self = this;
    	groupLevel = groupLevel || 0;
        var result = [];
        var $tbody = $('<tbody>');
        _.each(data, function (group) {
            if (!$tbody) {
                $tbody = $('<tbody>');
            }
            $tbody.append(self._renderGroupRow(group, groupLevel));
            if (group.data.length) {
                result.push($tbody);
                // render an opened group
                if (group.groupedBy.length) {
                    // the opened group contains subgroups
                    result = result.concat(self._renderGroups(group.data, groupLevel + 1));
                } else {
                    // the opened group contains records
                    var $records = _.map(group.data, function (record,index) {
                    	//Nilesh
                    	if (_self.mode !== 'edit' || _self.hasSelectors){
                    		return self._renderRow(record).prepend($("<th class='o_list_row_count_sheliya'>").html(index+1)); //.prepend($('<td>'));
                    	}
                    	else{
                    		return self._renderRow(record);
                    	}

                    });
                    result.push($('<tbody>').append($records));
                }
                $tbody = null;
            }
        });
        if ($tbody) {
            result.push($tbody);
        }
        return result;
    },

});
});
