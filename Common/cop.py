import xlsxwriter
import time
from ZDBM.Common.configure import *

class Report:

    def get_format(self,wd, option):
        return wd.add_format(option)
    # 设置居中

    def get_format_center(self,wb,num=1):
        return wb.add_format({'align': 'center','valign': 'vcenter','border':num})

    def set_border_(self,wb, num=1):
        return wb.add_format({}).set_border(num)
    # 写数据

    def write_center(self,worksheet, cl, data, wb):
        return worksheet.write(cl, data, self.get_format_center(wb))

    def init(self,data,data1,score):
        self.workbook = xlsxwriter.Workbook('../Data/ZDBM接口测试报告.xlsx')
        # print(self.workbook)
        self.worksheet = self.workbook.add_worksheet("ZDBM接口测试总况")
        self.worksheet2 = self.workbook.add_worksheet("ZDBM接口测试详情")
        # 设置列行的宽高
        self.worksheet.set_column("A:A", 15)
        self.worksheet.set_column("B:B", 20)
        self.worksheet.set_column("C:C", 20)
        self.worksheet.set_column("D:D", 20)
        self.worksheet.set_column("E:E", 20)
        self.worksheet.set_column("F:F", 20)
        self.worksheet.set_column("F:F", 20)
        self.worksheet.set_row(1, 30)
        self.worksheet.set_row(2, 30)
        self.worksheet.set_row(3, 30)
        self.worksheet.set_row(4, 30)
        self.worksheet.set_row(5, 30)
        self.worksheet.set_row(6, 30)

        define_format_H1 = self.get_format(self.workbook, {'bold': True, 'font_size': 18})
        define_format_H2 = self.get_format(self.workbook, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("#70DB93")
        define_format_H2.set_color("#ffffff")
        # Create a new Chart object.

        self.worksheet.merge_range('A1:F1', 'ZDBM接口测试报告总概况', define_format_H1)
        self.worksheet.merge_range('A2:F2', 'ZDBM接口测试概括', define_format_H2)
        self.worksheet.merge_range('A3:A6', '项目图片', self.get_format_center(self.workbook))

        self.write_center(self.worksheet, "B3", '项目名称', self.workbook)
        self.write_center(self.worksheet, "B4", '项目版本', self.workbook)
        self.write_center(self.worksheet, "B5", '运行环境', self.workbook)
        self.write_center(self.worksheet, "B6", '测试网络', self.workbook)


        self.write_center(self.worksheet, "C3", data['test_name'], self.workbook)
        self.write_center(self.worksheet, "C4", data['test_version'], self.workbook)
        self.write_center(self.worksheet, "C5", data['test_pl'], self.workbook)
        self.write_center(self.worksheet, "C6", data['test_net'], self.workbook)

        self.write_center(self.worksheet, "D3", "用例总数", self.workbook)
        self.write_center(self.worksheet, "D4", "通过总数", self.workbook)
        self.write_center(self.worksheet, "D5", "失败总数", self.workbook)
        self.write_center(self.worksheet, "D6", "测试日期", self.workbook)

        self.write_center(self.worksheet, "E3", data1['test_sum'], self.workbook)
        self.write_center(self.worksheet, "E4", data1['test_success'], self.workbook)
        self.write_center(self.worksheet, "E5", data1['test_failed'], self.workbook)
        self.write_center(self.worksheet, "E6", data1['test_date'], self.workbook)

        self.write_center(self.worksheet, "F3", "分数", self.workbook)


        self.worksheet.merge_range('F4:F6', '%s'%score, self.get_format_center(self.workbook))

        self.pie(self.workbook, self.worksheet)

     # 生成饼形图
    def pie(self,wob, wos):
        chart1 = wob.add_chart({'type': 'pie'})
        chart1.add_series({
            'name': 'ZDBM接口测试统计',
            'categories': '=ZDBM接口测试总况!$D$4:$D$5',
            'values': '=ZDBM接口测试总况!$E$4:$E$5',
        })
        chart1.set_title({'name': 'ZDBM接口测试统计'})
        chart1.set_style(10)
        wos.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})

    def test_detail(self,data,tmp,row):

        # 设置列行的宽高
        self.worksheet2.set_column("A:A", 30)
        self.worksheet2.set_column("B:B", 20)
        self.worksheet2.set_column("C:C", 20)
        self.worksheet2.set_column("D:D", 20)
        self.worksheet2.set_column("E:E", 50)
        self.worksheet2.set_column("F:F", 20)
        self.worksheet2.set_column("G:G", 20)
        self.worksheet2.set_column("H:H", 20)
        for i in range(1,(row+2)):
            self.worksheet2.set_row(i, 30)
        self.worksheet2.merge_range('A1:G1', '测试详情', self.get_format(self.workbook, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': '#70DB93', 'font_color': '#ffffff'}))
        self.write_center(self.worksheet2, "A2", '模块名', self.workbook)
        self.write_center(self.worksheet2,"B2", '类名', self.workbook)
        self.write_center(self.worksheet2,"C2", '方法名', self.workbook)
        self.write_center(self.worksheet2,"D2", '用例编号', self.workbook)
        self.write_center(self.worksheet2,"E2", '预期值', self.workbook)
        self.write_center(self.worksheet2,"F2", '实际值', self.workbook)
        self.write_center(self.worksheet2,"G2", '测试结果', self.workbook)
        # self.write_center(self.worksheet2,"H2", '测试结果', self.workbook)

        temp = tmp+2
        for item in data:
            self.write_center(self.worksheet2,"A"+str(temp), item["t_id"], self.workbook)
            self.write_center(self.worksheet2,"B"+str(temp), item["t_mod"], self.workbook)
            self.write_center(self.worksheet2,"C"+str(temp), item["t_obj"], self.workbook)
            self.write_center(self.worksheet2,"D"+str(temp), item["t_mtd"], self.workbook)
            # self.write_center(self.worksheet2,"E"+str(temp), item["t_param"], self.workbook)
            self.write_center(self.worksheet2,"E"+str(temp), item["t_hope"], self.workbook)
            self.write_center(self.worksheet2,"F"+str(temp), item["t_actual"], self.workbook)
            self.write_center(self.worksheet2,"G"+str(temp), item["t_result"], self.workbook)
            temp = temp-1

        self.worksheet.hide_gridlines(2)    # 隐藏网格线
        self.worksheet2.hide_gridlines(2)   # 隐藏网格线

    def test_report(self):
        try:
            data = []
            m = 0
            with open(r'..\Data\ZDBM接口测试结果.txt', 'r', encoding='utf-8') as f:
                result = f.readlines()
            for res in result:
                res = eval(res)
                if res[-1] == '测试成功':
                    m += 1
                print(res[0],res[1],res[2],res[3],res[4],res[5],res[-1])
                content = {"t_id": res[0],
                           "t_mod": res[1],
                           "t_obj": res[2],
                           "t_mtd": res[3],
                           "t_hope": res[4],
                           "t_actual": str(res[5]),
                           "t_result": res[-1]
                           }
                data.append(content)
            data_title = {"test_name": "备份一体机", "test_version": ZDBM_VERSION, "test_pl": "win10", "test_net": "公司内网"}
            data_re = {"test_sum": (len(result)), "test_success": m, "test_failed": ((len(result)) - m),
                       "test_date": time.strftime("%Y-%m-%d  %H:%M:%S")}
            self.r = Report()
            try:
                print(len(result) , m)
                self.r.init(data_title, data_re, int(m * 100 / len(result)))
                self.r.test_detail(data, len(result), len(data))
                self.workbook.close()

            except Exception:
                pass
        finally:
            try:
                self.workbook.close()
            except Exception:
                pass



if __name__ == '__main__':
    Report().test_report()
