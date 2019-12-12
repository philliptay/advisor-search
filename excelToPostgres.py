import os
import psycopg2
import pandas as pd
from flask import Flask


def main():
    # filename = 'Cos Department Data'
    # conn = psycopg2.connect(database='advisordb', user='admin', password='thesissearchboyz420', host='localhost', port='5432')
    # cursor = conn.cursor()
    # wb = pd.read_excel(filename+'.xlsx')
    # for i, row in wb.iterrows():
    #
    #     profsStmt = 'INSERT INTO profs (prof_id, name, bio, email) VALUES (%s,%s,%s,%s)'
    #     cursor.execute(profsStmt, (i, row['name'], row['bio'], row['email']+'@cs.princeton.edu'))
    #
    #     if not pd.isna(row['areas']):
    #         areasList = row['areas'].replace(';', ',').split(', ')
    #         for area in areasList:
    #             areaStmt = 'INSERT INTO areas (area, prof_id) VALUES (%s,%s)'
    #             cursor.execute(areaStmt, (area.strip().lower(), i))
    #
    #     if not pd.isna(row['Research Projects']):
    #         projsList = row['Research Projects'].replace(';', ',').split(', ')
    #         for proj in projsList:
    #             projStmt = 'INSERT INTO projects (title, prof_id) VALUES (%s,%s)'
    #             cursor.execute(projStmt, (proj.strip().lower(), i))
    #
    #     if not pd.isna(row['Past Theses Advised (Titles)']):
    #         titlesList = row['Past Theses Advised (Titles)'].split(';')
    #         linksList = row['Past Theses Advised (Links)'].split(';')
    #         for j in range(len(titlesList)):
    #             thesisStmt = 'INSERT INTO past_theses (title, link, prof_id) VALUES (%s,%s,%s)'
    #             cursor.execute(thesisStmt, (titlesList[j].strip(), linksList[j].strip(), i))

    profPics = {
        'Aarti Gupta': 'https://live.staticflickr.com/65535/49180373052_77e070b52a_n.jpg',
        'Adam Finkelstein': 'https://live.staticflickr.com/65535/49174808528_55680f30e5_n.jpg',
        'Alan Kaplan': 'https://live.staticflickr.com/65535/49174827063_25053c72cf_n.jpg',
        'Amit Levy': 'https://live.staticflickr.com/65535/49179992102_0d98b2bb34_n.jpg',
        'Andrew Appel': 'https://live.staticflickr.com/65535/49179784736_60eaac7bde_n.jpg',
        'Arvind Narayanan': 'https://live.staticflickr.com/65535/49179784711_637259a4b4_n.jpg',
        'Barbara Engelhardt': 'https://live.staticflickr.com/65535/49179992077_74492d2c16_n.jpg',
        'Bernard Chazelle': 'https://live.staticflickr.com/65535/49179293028_bef3e4930c_n.jpg',
        'Brian Kernighan': 'https://live.staticflickr.com/65535/49179784656_afdd306907_n.jpg',
        'Christiane Fellbaum': 'https://live.staticflickr.com/65535/49179784631_705b6aa1c5_n.jpg',
        'Christopher Moretti': 'https://live.staticflickr.com/65535/49179329783_eac0ed1d8d_n.jpg',
        'Daniel Leyzberg': 'https://live.staticflickr.com/65535/49179992022_209f93deb7_n.jpg',
        'Danqi Chen': 'https://live.staticflickr.com/65535/49179292963_7c04f27026_n.jpg',
        'David August': 'https://live.staticflickr.com/65535/49179292933_c4246282e8_n.jpg',
        'David Dobkin': 'https://live.staticflickr.com/65535/49179292923_a84d098dab_n.jpg',
        'David Walker': 'https://live.staticflickr.com/65535/49179784551_8c893c24be_n.jpg',
        'Edward Felten': 'https://live.staticflickr.com/65535/49180084021_ae3a35865e_n.jpg',
        'Elad Hazan': 'https://live.staticflickr.com/65535/49180290722_4fbff02a98_n.jpg',
        'Gillat Kol': 'https://live.staticflickr.com/65535/49180084006_d8052569e9_n.jpg',
        'Iasonas Petras': 'https://live.staticflickr.com/65535/49179593928_7ec9888b7f_n.jpg',
        'Ibrahim Albluwi': 'https://live.staticflickr.com/65535/49179593918_7a0dbb089c_n.jpg',
        'Jack Brassil': 'https://live.staticflickr.com/65535/49180083976_a6d1450990_n.jpg',
        'Jaswinder Singh': 'https://live.staticflickr.com/65535/49180083951_c2548d94f4_n.jpg',
        'Jennifer Rexford': 'https://live.staticflickr.com/65535/49180083941_578ac2b7fd_n.jpg',
        'Jérémie Lumbroso': 'https://live.staticflickr.com/65535/49180083921_4ed476f389_n.jpg',
        'Jia Deng': 'https://live.staticflickr.com/65535/49180290647_89433dea8a_n.jpg',
        'Jonathan Mayer': 'https://live.staticflickr.com/65535/49180083911_9822eb3e87_n.jpg',
        'Kai Li': 'https://live.staticflickr.com/65535/49180083891_3249154470_n.jpg',
        'Karthik Narasimhan': 'https://live.staticflickr.com/65535/49180290627_398207ef13_n.jpg',
        'Kevin Wayne': 'https://live.staticflickr.com/65535/49180083871_98501dd81b_n.jpg',
        'Kyle Jamieson': 'https://live.staticflickr.com/65535/49180083851_98f7f3852b_n.jpg',
        'Larry Peterson': 'https://live.staticflickr.com/65535/49179593813_ddbc16a5fe_n.jpg',
        'Maia Ginsburg': 'https://live.staticflickr.com/65535/49180290562_ff9ebcdf3f_n.jpg',
        'Margaret Martonosi': 'https://live.staticflickr.com/65535/49180083826_f51f8a88e2_n.jpg',
        'Mark Braverman': 'https://live.staticflickr.com/65535/49179593763_aa94709bd9_n.jpg',
        'Mark Zhandry': 'https://live.staticflickr.com/65535/49179593738_3c5752df91_n.jpg',
        'Matthew Weinberg': 'https://live.staticflickr.com/65535/49180083816_d5b1dbcc24_n.jpg',
        'Michael Freedman': 'https://live.staticflickr.com/65535/49179593718_9047931257_n.jpg',
        'Mona Singh': 'https://live.staticflickr.com/65535/49180290507_a4508db633_n.jpg',
        'Olga Russakovsky': 'https://live.staticflickr.com/65535/49180083786_6c1413efdc_n.jpg',
        'Olga Troyanskaya': 'https://live.staticflickr.com/65535/49180083771_fa4848b7cb_n.jpg',
        'Ran Raz': 'https://live.staticflickr.com/65535/49179593678_72cbd10902_n.jpg',
        'Robert Dondero': 'https://live.staticflickr.com/65535/49179593663_dcb001a4b3_n.jpg',
        'Robert Fish': 'https://live.staticflickr.com/65535/49180083746_3545d49ccd_n.jpg',
        'Robert Schapire': 'https://live.staticflickr.com/65535/49180290447_35de556377_n.jpg',
        'Robert Sedgewick': 'https://live.staticflickr.com/65535/49180083736_a8d26b83b0_n.jpg',
        'Robert Tarjan': 'https://live.staticflickr.com/65535/49179593638_3bc0a2698d_n.jpg',
        'Ryan Adams': 'https://live.staticflickr.com/65535/49179593623_b11912d152_n.jpg',
        'Sanjeev Arora': 'https://live.staticflickr.com/65535/49180083696_ae484b10df_n.jpg',
        'Sebastian Seung': 'https://live.staticflickr.com/65535/49180083686_dacfb2ef3d_n.jpg',
        'Szymon Rusinkiewicz': 'https://live.staticflickr.com/65535/49180083671_f3c7999fec_n.jpg',
        'Tom Griffiths': 'https://live.staticflickr.com/65535/49179593578_43e007ccc2_n.jpg',
        'Wyatt Lloyd': 'https://live.staticflickr.com/65535/49180083646_05531b4e1a_n.jpg',
        'Xiaoyan Li': 'https://live.staticflickr.com/65535/49180083641_fa065ee330_n.jpg',
        'Yoram Singer': 'https://live.staticflickr.com/65535/49180290367_31ec461978_n.jpg',
        'Zachary Kincaid': 'https://live.staticflickr.com/65535/49180290337_a95fe9f7d5_n.jpg',
        'Zeev Dvir': 'https://live.staticflickr.com/65535/49180290322_14fc97ca95_n.jpg',
    }

    DATABASE_URL = 'postgres://mzehsxrhlmmrdp:7229a3ce7cdddcfd25d960016bab27a25ecd1163a471263f73d2c64d78f15d70@ec2-174-129-252-252.compute-1.amazonaws.com:5432/d56v6b7trhtuts'
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = conn.cursor()
    for name in profPics:
        stmt = "UPDATE profs SET pic_links = %s WHERE name = %s;"
        cursor.execute(stmt, (profPics.get(name), name))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
