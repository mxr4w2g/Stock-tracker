import xlsxwriter
import xlrd #excel module,read excel files 


def write_to_database(item_name,buy_price,sell_price,quantity):
    existing_data = read_from_database()
    


    wb = xlsxwriter.Workbook("./transactions.xlsx")
    ws = wb.add_worksheet()         #adding worksheet to the workbook

 

    #existing data 
    if len(existing_data) != 0:
        for row in range(len(existing_data)):
            ws.write(row,0,existing_data[row][0])   #in current row in the 0 column, writing the existing data in that same row in column 0(whatever a1 was in old sheet copy over to a1 in the new excel sheet)
            ws.write(row,1,existing_data[row][1])    
            ws.write(row,2,existing_data[row][2])
            ws.write(row,3,existing_data[row][3])
            ws.write(row,4,existing_data[row][4])

    #headers 

    ws.write(0,0,"ID")
    ws.write(0,1,"Item name ")
    ws.write(0,1,"Buy price ")
    ws.write(0,1,"Sell price")
    ws.write(0,1,"Quantity ")

    #new data
    if len(existing_data) == 0: #if data has length of 0, then write everything in 2nd row,otherwise if we have exisiting data go to else 
        ws.write(1,0,1)   
        ws.write(1,1,item_name)
        ws.write(1,2,buy_price)
        ws.write(1,3,sell_price)
        ws.write(1,4,quantity)
    else:
        ws.write(len(existing_data),0,len(existing_data))   
        ws.write(len(existing_data),1,item_name)
        ws.write(len(existing_data),2,buy_price)
        ws.write(len(existing_data),3,sell_price)
        ws.write(len(existing_data),4,quantity)

    #save file
    wb.close()      #close the file and save


def read_from_database():
    wb = xlrd.open_workbook("./transactions.xlsx") # open the file -->(transactions is the workbook name) 
    ws=wb.sheet_by_index(0) #look at the sheet within the file -->(0 is index of the first sheet)

    #Columns are [ID,Item name, buy price, sell price , quantity]

    all_rows = []                                       #all rows will be stored in this excel list 
    for i in range(ws.nrows):       #loop through every row 
        current_row  = []                                       #make master list of all the rows 
        current_row.append(ws.cell_value(i,0))  #[THIS GETS ID OF CURRENT ROW]. i is the y(column) , 0 is x(row)
        current_row.append(ws.cell_value(i,1))
        current_row.append(ws.cell_value(i,2))
        current_row.append(ws.cell_value(i,3))
        current_row.append(ws.cell_value(i,4))    
        all_rows.append(current_row)        #get all the data of what is looped through, add to the master list

    return all_rows     #return the master list

#what this code does is give us every single cell that is not blank in our excel file