<div style="width:100%;">
<table>
	%for y in range(9):
		<tr>
		%for x in range(9):
			%id = chr(ord('a')+y) + str(x+1)
				%if x % 3 == 0 and y % 3 == 0:
					<td class="vert-hor-3 content">
				%elif x % 8 == 0  and y % 3 == 0 and y != 8:
					<td class="vert-hor-8 content">
				%elif x % 3 == 0 and y % 3 != 0 and y != 8:
					<td class="vert-3 content">
				%elif x % 3 != 0 and y % 3 == 0 :
					<td class="hor-3 content">

				%elif x % 8 == 0 and y % 8 != 0 :
					<td class="vert-8 content">
				%elif x % 8 != 0 and y % 8 == 0 and x % 3 == 0:
					<td class="hor-3-bot content">
				%elif x % 8 != 0 and y % 8 == 0 :
					<td class="hor-8 content">
				%elif x == 0 and y == 8:
					<td class="hor-3-bot content">
				%elif x == 8 and y == 8:
					<td class="hor-3-bot-right content">
				%else:
					<td class="content">
				%end

				<input type="tel" class="cell center"

				%if (id in board):
					value={{board[id][0]}}

					%if (board[id][1] == False):
						readonly
						style="background-color:black"
						immutable="immutable"
					%end

				%else:
					value=""
				%end

				name={{id}}
				id={{id}}
				maxlength="1" size="1"
				onchange="updateCellValue(this.id, this.value)"
				onkeypress="return validateInput(event)"/>
				</div></td>
		%end
		<tr>
	%end
</table>
</div>
