import datetime as dt
from datetime import datetime

import pandas as pd


def tm(strtime):
	tm = datetime.strptime(strtime, '%H:%M')
	return tm


def problem(self, answers):
	problem = 0 if int(answers[0]) == 0 \
		else 5 if int(answers[0]) == 2 else 10
	return problem


def duration(self, answers):

	def duration_cats(dif):
		result = (
			0 if dif<300 or dif>600 else\
			1 if dif<360 or dif>540 else\
			2 if dif<420 or dif>480 else\
			3 if dif>=420 or dif<=480 else\
			print('Bad duration number!'))
		return result

	day = tm(answers[3])
	end = tm(answers[6])

	dif_day = (day-tm('00:00')).seconds/60
	dif_end = (end-tm('00:00')).seconds/60
	duration = duration_cats(dif_day) + duration_cats(dif_end)

	return duration


def timing(self, answers):

	def mp_cats(mp):
		dif = (mp-tm('00:00')-dt.timedelta(days=1)).seconds/60
		result = (
			0 if dif<=45 or dif>=255 else\
			1 if dif<=60 or dif>=240 else\
			2 if dif<=75 or dif>=225 else\
			3 if dif<=90 or dif>=210 else\
			4 if dif<=105 or dif>=195 else\
			5 if dif<=120 or dif>=180 else\
			6 if dif<=135 or dif>=165 else\
			7)

		return result

	weeksleep, weekwake, endsleep, endwake = \
	tm(answers[1]), tm(answers[2]), tm(answers[4]), tm(answers[5])

	a8 = int(answers[7])
	a9 = int(answers[8])

	q8 = 0 if a8==0 or a8==5 else\
		 1 if a8==1 or a8==4 else\
		 2 if a8==2 or a8==3 else\
		 print('Bad Q8 number')

	q9 = 0 if a9==0 or a9==3 else\
		 1 if a9==1 or a9==2 else\
		 print('Bad Q9 number')

	week_mp = mp_cats(weeksleep + (weekwake+dt.timedelta(days=1) - weeksleep) / 2)
	timing = q8+q9+week_mp

	return timing


def regularity(self, answers):

	weeksleep, weekwake, endsleep, endwake = \
	tm(answers[1]), tm(answers[2]), tm(answers[4]), tm(answers[5])

	week_mp = (weeksleep + (weekwake+dt.timedelta(days=1) - weeksleep) / 2)\
		-dt.timedelta(days=1)
	end_mp = (endsleep + (endwake+dt.timedelta(days=1) - endsleep) / 2)\
		-dt.timedelta(days=1)

	mp_dif = abs(week_mp-end_mp).seconds/60
	sd_dif = abs(tm(answers[3])-tm(answers[6])).seconds/60

	sjl = 0 if mp_dif>=90 else\
		  1 if mp_dif>=60 else\
		  2 if mp_dif>=30 else\
		  3

	sdd = 0 if sd_dif>=120 else\
		  1 if sd_dif>=90 else\
		  2 if sd_dif>=60 else\
		  3 if sd_dif>=30 else\
		  4
	regularity = sjl+sdd

	return regularity

def adequacy(self, answers):

	q10 = int(answers[9])
	q14 = 0 - int(answers[13])
	q15 = 3 - int(answers[14])
	adequacy = q10+q14+q15

	return adequacy

def insomnia(self, answers):

	q11 = 3 - int(answers[10])
	q12 = 3 - int(answers[11])
	q13 = 3 - int(answers[12])
	insomnia = q11+q12+q13

	return insomnia

class gss15:
    def __init__(self, id, answers):
        """
        Parameters
        ----------
        dataframe: pandas.DataFrame
            A pandas dataframe of the data to be scored.
            Run main_app.py or see the README for a template. 
        """
        self.id = id

        self.answers = answers

        self.problem = problem(self, answers)
        self.duration = duration(self, answers)
        self.timing = timing(self, answers)
        self.regularity = regularity(self, answers)
        self.adequacy = adequacy(self, answers)
        self.insomnia = insomnia(self, answers)

        subdomains = [self.problem,
					  self.duration,
					  self.timing,
					  self.regularity,
					  self.adequacy,
					  self.insomnia]

        self.total = sum(subdomains)

    
if __name__ == "__main__":
	df = pd.read_csv('data.csv')
	domains = [
               'problem',
               'duration',
               'timing',
               'regularity',
               'adequacy',
               'insomnia',
               'total'
    ]
	for d in domains: df[f"{d}_score"] = ''
    
	for i, r in df.iterrows():
		px = r['px_id']
		answers = [r[f"q_{c+1}"] for c in range(15)]
		g = gss15(id=px, answers=answers)
		for d in domains:
			df[f"{d}_score"][i] = getattr(g, d)

	df.to_csv('data.csv', index=False)
