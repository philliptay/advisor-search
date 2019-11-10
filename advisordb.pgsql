--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: areas; Type: TABLE; Schema: public; Owner: ptaylor
--

CREATE TABLE public.areas (
    area character varying(100),
    prof_id integer NOT NULL
);


ALTER TABLE public.areas OWNER TO ptaylor;

--
-- Name: areas_prof_id_seq; Type: SEQUENCE; Schema: public; Owner: ptaylor
--

CREATE SEQUENCE public.areas_prof_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.areas_prof_id_seq OWNER TO ptaylor;

--
-- Name: areas_prof_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ptaylor
--

ALTER SEQUENCE public.areas_prof_id_seq OWNED BY public.areas.prof_id;


--
-- Name: profs; Type: TABLE; Schema: public; Owner: ptaylor
--

CREATE TABLE public.profs (
    prof_id integer NOT NULL,
    bio character varying(2000),
    email character varying(50),
    name character varying(50)
);


ALTER TABLE public.profs OWNER TO ptaylor;

--
-- Name: profs_prof_id_seq; Type: SEQUENCE; Schema: public; Owner: ptaylor
--

CREATE SEQUENCE public.profs_prof_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profs_prof_id_seq OWNER TO ptaylor;

--
-- Name: profs_prof_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ptaylor
--

ALTER SEQUENCE public.profs_prof_id_seq OWNED BY public.profs.prof_id;


--
-- Name: projects; Type: TABLE; Schema: public; Owner: ptaylor
--

CREATE TABLE public.projects (
    title character varying(200),
    description character varying(200),
    prof_id integer NOT NULL
);


ALTER TABLE public.projects OWNER TO ptaylor;

--
-- Name: projects_prof_id_seq; Type: SEQUENCE; Schema: public; Owner: ptaylor
--

CREATE SEQUENCE public.projects_prof_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.projects_prof_id_seq OWNER TO ptaylor;

--
-- Name: projects_prof_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ptaylor
--

ALTER SEQUENCE public.projects_prof_id_seq OWNED BY public.projects.prof_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: ptaylor
--

CREATE TABLE public.users (
    username character varying(50) NOT NULL,
    password character varying(50)
);


ALTER TABLE public.users OWNER TO ptaylor;

--
-- Name: areas prof_id; Type: DEFAULT; Schema: public; Owner: ptaylor
--

ALTER TABLE ONLY public.areas ALTER COLUMN prof_id SET DEFAULT nextval('public.areas_prof_id_seq'::regclass);


--
-- Name: profs prof_id; Type: DEFAULT; Schema: public; Owner: ptaylor
--

ALTER TABLE ONLY public.profs ALTER COLUMN prof_id SET DEFAULT nextval('public.profs_prof_id_seq'::regclass);


--
-- Name: projects prof_id; Type: DEFAULT; Schema: public; Owner: ptaylor
--

ALTER TABLE ONLY public.projects ALTER COLUMN prof_id SET DEFAULT nextval('public.projects_prof_id_seq'::regclass);


--
-- Data for Name: areas; Type: TABLE DATA; Schema: public; Owner: ptaylor
--

COPY public.areas (area, prof_id) FROM stdin;
programming languages	0
compilers	0
formal verification	0
program analysis	0
logic decision procedures.	0
graphics	1
vision	1
human-computer interaction	1
mobile software	2
middleware and protocols	2
communication and networking for consumer applications and services	2
software engineering.	2
security	3
privacy	3
systems	3
policy	4
programming languages	4
compilers	4
security	4
privacy	4
software verification	4
computer security	4
programming languages	4
compilers.	4
information privacy	5
security	5
fairness in machine learning	5
cryptocurrencies	5
tech policy	5
big data	5
computational biology	6
machine learning	6
bayesian statistics	6
statistical genetics	6
quantitative genetics	6
theory	7
natural algorithms	7
dynamical systems	7
dynamic networks	7
computational geometry	7
discrepancy theory	7
policy	8
programming languages / compilers	8
security	8
privacy	8
application-specific languages	8
document preparation	8
user interfaces	8
software tools	8
programming methodology.	8
lexical semantics	9
syntactic alternations	9
computational linguistics	9
distributed systems	10
computer science education	10
machine learning	12
natural language processing	12
computer architecture	13
programming languages	13
compilers	13
systems	13
computer architecture and compilers	13
graphics	14
vision	14
human-computer interaction	14
policy	14
visualization	14
pervasive computing	14
software engineering.	14
programming languages	15
type systems	15
compilers	15
domain-specific languages	15
and software-defined networking.	15
policy	17
security	17
privacy	17
network software	17
machine learning	18
theoretical foundations of machine learning	18
design and analysis of efficient algorithms for machine learning and mathematical optimization.	18
graphics	19
vision	19
human-computer interaction	19
computational imaging	19
computer vision	19
computer graphics	19
optics	19
theory	20
quantum computation	21
information-based complexity	21
parallel computing systems and applications	24
system software and programming environments for multiprocessors	24
computational biology	24
networking	25
network virtualization	25
internet measurement	25
network management	25
network troubleshooting.	25
probabilistic algorithms	26
data streaming	26
data structures	26
analysis of algorithms	26
analytic combinatorics	26
graphics	27
vision	27
human-computer interaction	27
machine learning	27
technology law and policy	28
with emphasis on national security	28
criminal procedure	28
consumer privacy	28
network management	28
and online speech	28
parallel architectures and systems	29
distributed systems	29
operating systems	29
computational biology	29
computer architecture	29
systems	29
machine learning	30
natural language processing	30
algorithms	31
theory	31
graph theory	31
systems	32
networking	32
wireless systems	32
internet of things	32
networked systems	33
communication protocols	33
operating systems	33
computer architecture	35
power-aware computing	35
and mobile computing	35
policy	35
security & privacy	35
systems	35
complexity theory	36
algorithms	36
game theory	36
machine learning	36
healthcare	36
medicine	36
cryptography	37
privacy	37
quantum computing	37
security	37
theory	37
economics/computation	38
policy	38
theory	38
policy	39
security	39
privacy	39
systems	39
distributed systems	39
security	39
networking.	39
computational molecular biology	40
machine learning	40
algorithms.	40
graphis/vision/human-computer interaction	41
machine learning	41
policy	41
bioinformatics	42
analysis of large-scale biological data sets	42
algorithms for integration of data from multiple data sources	42
visualization of biological data	42
machine learning methods in bioinformatics.	42
theory	43
networking and telecommunications	45
computer-human interaction	45
online learning and moocs	45
r&d innovation methodologies	45
machine learning	46
scientific analysis of algorithms	47
analytic combinatorics	47
theory	47
data structures	48
graph algorithms	48
combinatorial optimization	48
computational complexity	48
computational geometry	48
parallel algorithms.	48
machine learning	49
artificial intelligence	49
computational statistics	49
machine learning	50
natural language processing	50
theory	50
uses of randomness in complexity theory and algorithms	50
np-hard problems	50
cryptography.	50
computational biology	51
machine learning	51
computer graphics	52
acquisition of 3d shape	52
reflectance	52
and appearance of real-world objects	52
machine learning	53
psychology	53
distributed systems	54
question answering	55
information retrieval	55
data mining	55
machine learning	55
machine learning	56
programming languages / compilers	57
programming languages	57
program analysis	57
program verification	57
automated reasoning	57
theory	58
math	58
\.


--
-- Data for Name: profs; Type: TABLE DATA; Schema: public; Owner: ptaylor
--

COPY public.profs (prof_id, bio, email, name) FROM stdin;
0	Aarti Gupta joined the Computer Science Department as a full professor in 2015. Before joining the department, she worked at NEC Labs America where she led a team in investigating new techniques for formal verification of software and hardware systems, contributing both to their foundations and to successful industrial deployment. The impact of this work was recognized through NEC Technology Commercialization Awards that she received in 2005, 2006 and 2012. Professor Gupta received her Ph.D. in computer science from Carnegie Mellon University in 1994 after earning a master’s degree in computer engineering from Rensselaer Polytechnic Institute and a bachelor’s in electrical engineering from the Indian Institute of Technology in New Delhi. She has served as an Associate Editor for Formal Methods in System Design (since 2005) and for the ACM Transactions on Design Automation of Electronic Systems (2008-2012). She has served as program chair and on the steering committees of the International Conference on Computer Aided Verification (CAV) and the International Conference on Formal Methods in Computer Aided Design (FMCAD).	aartig@cs.princeton.edu	Aarti Gupta
1	Adam Finkelstein joined the Department of Computer Science in 1997 as an assistant and then associate professor, and became a full professor in 2001.  He is one of the organizers of the art of science exhibition at Princeton. He took a sabbatical during the 2010-11 academic year at the Adobe Creative Technologies Lab, where he was a visiting researcher; and in 2003-04 at Pixar Animation Studios, where he worked on lighting tools. Finkelstein earned his masters and doctoral degrees from the University of Washington. He studied physics and computer science at Swathmore College, and was then a software engineer at Tibco in the late 1980's. His awards include the NSF CAREER Award and an Alfred P. Sloan Fellowship, and he is a Fellow of the ACM.	af@cs.princeton.edu	Adam Finkelstein
2	Alan Kaplan joined the Department of Computer Science as a Lecturer in September 2014.   His career spans academic research to industrial R&D to technology startup/entrepreneurship and he has over twenty years experience leading research and product development involving mobile software.\n\nPrior to joining Princeton, Dr. Kaplan was the Chief Technology Officer for Drakontas, a software company that develops a mobile command, control and collaboration platform, called DragonForce, for law enforcement, public safety and first responder agencies.  \n\nDr. Kaplan was formerly Department Head of Middleware and Software Technologies at the Panasonic Princeton Research Laboratory. Prior to Panasonic, he held faculty positions in computer science departments at Clemson University and Flinders University of South Australia. Dr. Kaplan holds a Ph.D. and M.S. in Computer Science from the University of Massachusetts Amherst and a B.S. in Computer Science from Duke University.  \n\nHe has significant experience in international standards development organizations, such as Open Mobile Alliance, Java Community Process and IEEE. In addition, he is an active volunteer in the IEEE Communications Society, serving on the Steering Committee for the Consumer Communications and Network Conference (IEEE CCNC).  He  recently (2016-2017) served as Chair of the IEEE Communications Society GIMS (Globecom & ICC Management and Strategy) Committee.	ak18@cs.princeton.edu	Alan Kaplan
3	Amit Levy is an Assistant Professor in the Computer Science Department. He received his BSc in computer science and economics from the University of Washington in 2009, and his Ph.D. in computer science from Stanford University in 2018.	aalevy@cs.princeton.edu	Amit Levy
4	Andrew Appel is Eugene Higgins Professor Computer Science, and served from 2009-2015 as Chair of the department. His research is in software verification, computer security, programming languages and compilers, and technology policy. He received his A.B. summa cum laude in physics from Princeton in 1981, and his Ph.D. in computer science from Carnegie Mellon University in 1985. Professor Appel has been editor in chief of ACM Transactions on Programming Languages and Systems and is a fellow of the ACM (Association for Computing Machinery). He has worked on fast N-body algorithms (1980s), Standard ML of New Jersey (1990s), Foundational Proof-Carrying Code (2000s), and the Verified Software Toolchain (2010s).	appel@cs.princeton.edu	Andrew Appel
5	Arvind Narayanan is an Associate Professor of Computer Science at Princeton. He leads the Princeton Web Transparency and Accountability Project to uncover how companies collect and use our personal information. Narayanan also leads a research team investigating the security, anonymity, and stability of cryptocurrencies as well as novel applications of blockchains. He co-created a Massive Open Online Course as well as a textbook on Bitcoin and cryptocurrency technologies. His doctoral research showed the fundamental limits of de-identification, for which he received the Privacy Enhancing Technologies Award.\n\nNarayanan is an affiliated faculty member at the Center for Information Technology Policy at Princeton and an affiliate scholar at Stanford Law School's Center for Internet and Society. You can follow him on Twitter at @random_walker.	arvindn@cs.princeton.edu	Arvind Narayanan
6	Barbara E. Engelhardt, an associate professor, joined the Princeton Computer Science Department in 2014 from Duke University, where she had been an assistant professor in Biostatistics and Bioinformatics and Statistical Sciences.  She graduated from Stanford University and received her Ph.D. from the University of California, Berkeley, advised by Professor Michael Jordan. She did postdoctoral research at the University of Chicago, working with Professor Matthew Stephens, and three years at Duke University as an assistant professor. Interspersed among her academic experiences, she spent two years working at the Jet Propulsion Laboratory, a summer at Google Research, and a year at 23andMe, a DNA ancestry service. Professor Engelhardt received an NSF Graduate Research Fellowship, the Google Anita Borg Memorial Scholarship, and the Walter M. Fitch Prize from the Society for Molecular Biology and Evolution. As a faculty member, she received the NIH NHGRI K99/R00 Pathway to Independence Award, a Sloan Faculty Fellowship, and an NSF CAREER Award. Professor Engelhardt’s research interests involve developing statistical models and methods for the analysis of high-dimensional biomedical data, with a goal of understanding the underlying biological mechanisms of complex phenotypes and human disease.	bee@cs.princeton.edu	Barbara Engelhardt
7	Bernard Chazelle is the Eugene Higgins Professor of Computer Science at Princeton University, where he has been on the faculty since 1986.  He has held research and faculty positions at College de France, Carnegie-Mellon University, Brown University, Ecole Polytechnique, Ecole Normale Superieure, University of Paris, INRIA, Xerox Parc, DEC SRC, and NEC Research, where he was the president of the Board of Fellows for many years. He has served on the editorial board of more than a dozen scientific journals. He received his Ph.D in computer science from Yale University in 1980. The author of the book, "The Discrepancy Method," he is a fellow of the American Academy of Arts and Sciences, the European Academy of Sciences, and the recipients of three Best Paper awards from the scientific organization SIAM.	chazelle@cs.princeton.edu	Bernard Chazelle
8	Professor Brian W. Kernighan, who earned his doctoral degree in electrical engineering from Princeton in 1969, joined the department in 2000. Before returning to Princeton, he worked for 30 years at the Computing Science Research Center of Bell Laboratories, where he was head of the Computing Structures Research Department from 1981 to 2000.  Professor Kernighan was a member of the editorial board for Software―Practice & Experience, 1990-2009, and has been the adviser for the Addison-Wesley series on Professional Computing since 1990. His research Interests include software tools, application-oriented languages, programming methodology, user interfaces and technology education. He was elected to the National Academy of Engineering in 2002 and to the American Academy of Arts and Sciences in 2019.	bwk@cs.princeton.edu	Bryan Kernighan
9	Christiane Fellbaum is a senior research scholar in the Computer Science Department. A native of Brunswick, Germany, she received her Ph.D. in linguistics from Princeton in 1980 and completed a postdoctoral fellowship at the University of Paris. After several teaching and research positions, she returned to Princeton to work as a research scientist in 1987. She is the co-developer and current director of the WordNet project, and the co-founder and co-president of the Global WordNet Association. Her honors include the Wolfgang Paul-Prize of the German Humboldt Foundation (2001) and the Antonio Zampolli Prize (2006). Her research Interests include theoretical linguistics, computational and corpus linguistics, and natural language processing.	fellbaum@cs.princeton.edu	Christiane Fellbaum
10	Christopher Moretti is a lecturer in computer science at Princeton University. Prior to coming to Princeton in 2010, he earned his doctorate in computer science and engineering from the University of Notre Dame. At Princeton he has taught and developed for the CS I course (COS126), the systems-track CS II course (COS217), the functional programming course (COS326), and the project-based software engineering course (COS333). He has also served as an academic advisor for engineering freshman and upperclass computer science majors. His research interests focus on distributed computing and storage, and computer science education. He has directed junior and senior independent work research projects in these areas, as well as sports analytics, programming tools, and software engineering.	cmoretti@cs.princeton.edu	Christopher Moretti
11	Daniel Leyzberg joined the department as a lecturer in 2014 after earning his Ph.D. in computer science from Yale, where he also received a master’s. He did his undergraduate work in computer science and mathematics at Rensselaer Polytechnic Institute. His interests involve computer science education as well as human-computer or human-robot interaction, especially how people expect to use machines, how to build machines that conform to natural human communication patterns, and building machines that adapt to the needs of individual users. In addition to precepting, he is working on software tools to improve how teachers and students communicate about code.	dl9@cs.princeton.edu	Daniel Leyzberg
12	NaN	danqic@cs.princeton.edu	Danqi Chen
13	David I. August joined the department as a lecturer in 1999, became an assistant professor the next year, an associate professor in 2006 and a full professor in 2012. He earned his doctoral and master’s degrees in electrical and computer engineering from the University of Illinois at Urbana-Champaign.  Among his professional activities, Professor August was co-program chair for MICRO 2009, and he served on the program committees for ISCA 2007, PLDI 2008, MICRO 2010, ASPLOS 2011, and Top-Picks 2012.  His “Revisiting the Sequential Programming Model for the Multicore Era” was chosen for IEEE Micro’s Top-Picks special issue of papers "most relevant to industry and significant in contribution to the field of computer architecture" in 2007.  He also won the Best Paper Award for “Fault-tolerant Typed Assembly Language” at the 2007 ACM SIGPLAN Conference on Programming Language Design and Implementation (PLDI), in June 2007. His primary research interests are in synergistic compiler and microarchitecture design. 	august@cs.princeton.edu	David August
14	David Dobkin is the Phillip Y. Goldman '86 Professor in Computer Science, a professorship that was created through a gift from his former student and WebTV Networks founder Phillip Goldman. Professor Dobkin studied electrical engineering and mathematics at MIT and received master’s and doctoral degrees in applied mathematics from Harvard in 1971 and 1973. He joined the Princeton faculty as a professor of electrical engineering and computer science in 1981 after teaching at Yale and the University of Arizona. He became a professor of computer science when the department was formed in 1985, and he served as chair of the department from 1994 to 2003. He was dean of Princeton’s faculty from 2003 to 2014.\n\nHe received the Engineering Council's teaching award in 1990, is a fellow of the Association of Computing Machinery, and has been awarded a Guggenheim fellowship and a Fulbright grant. His research focuses on the interface between computational geometry and computer graphics. He has been an adviser and visiting researcher at companies such as Bell Labs, AT&T Research and Xerox as well as the governments of Denmark, Israel and Singapore. He also has served on the executive committee of the National Science Foundation's Center for Discrete Mathematics and Theoretical Computer Science as well as the foundation's Geometry Center. He serves on the editorial boards of several professional\njournals.	dpd@cs.princeton.edu	David Dobkin
15	David Walker joined the department in 2002, was granted tenure in 2008 and was appointed a full professor in 2013. He received his doctoral and master’s degrees in computer science from Cornell, and his bachelor’s from Queen’s University in Kingston, Ontario.  During sabbaticals from Princeton, he has served as a visiting researcher at Microsoft Research in Redmond (2008) and in Cambridge (2009), and as Associate Visiting Faculty at the University of Pennsylvania (2015-2016).  Professor Walker studies programming language theory, design and implementation, with an emphasis on the design of domain-specific languages.  His awards include an NSF Career Award, a Sloan Fellowship and the 2015 ACM SIGPLAN Robin Milner Young Researcher Award.  Together with his collaborators, he has also won a 10-year retrospective award for the most influential paper at ACM POPL 1998, a best paper award at ACM PLDI 2007, and a Community Award for his work at USENIX NSDI 2013.  He served as an associate editor for ACM TOPLAS from 2007-2015 and as program chair for ACM POPL in 2015.	dpw@cs.princeton.edu	David Walker
16	Donna Gabai, lecturer in General Computer Science, received her master’s degree in engineering from the University of Pennsylvania in 1980 and a master’s in teaching from Occidental College in 1998.	dgabai@cs.princeton.edu	Donna Gabai
55	Lecturer Xiaoyan Li earned her doctorate in computer science from the University of Massachusetts, Amherst, in 2006. Her main responsibility at Princeton is teaching, and she also supervises students on their junior independent work each semester. Her research interests include question answering, information retrieval, data mining and other applications of machine learning techniques.	xiaoyan@cs.princeton.edu	Xiaoyan Li
56	NaN	ysinger@cs.princeton.edu	Yoram Singer
17	Edward W. Felten is the Robert E. Kahn Professor of Computer Science and Public Affairs and the founding director of Princeton's Center for Information Technology Policy. In 2011-12 he served as the first chief technologist for the Federal Trade Commission. His research interests include computer security and privacy, especially relating to media and consumer products; and technology law and policy. He has published about 80 papers in the research literature and two books. His research on topics such as web security, copyright and copy protection, and electronic voting has been covered extensively in the popular press. His weblog, at freedom-to-tinker.com, is widely read for its commentary on technology, law and policy.\n\nProfessor Felten is a member of the National Academy of Engineering and the American Academy of Arts and Sciences, and is a fellow of the ACM. He has testified at House and Senate committee hearings on privacy, electronic voting and digital television. In 2004, Scientific American magazine named him to its list of 50 worldwide science and technology leaders.	felten@cs.princeton.edu	Edward Felten
18	Elad Hazan is a professor of computer science at Princeton university. He joined in 2015 from the Technion, where he had been an associate professor of operations research. His research focuses on the design and analysis of algorithms for basic problems in machine learning and optimization. Amongst his contributions are the co-development of the AdaGrad algorithm for training learning machines, and the first sublinear-time algorithms for convex optimization. He is the recipient of (twice) the IBM Goldberg best paper award in 2012 for contributions to sublinear time algorithms for machine learning, and in 2008 for decision making under uncertainty, a European Research Council grant , a Marie Curie fellowship and a Google Research Award (twice). He serves on the steering committee of the Association for Computational Learning and has been program chair for COLT 2015.	ehazan@cs.princeton.edu	Elad Hazan
19	Felix Heide is interested in the theory and application of computational imaging and computer vision systems. Researching imaging, vision and display systems end-to-end, Felix's work lies at the intersection of optics, machine learning, optimization, computer graphics and computer vision. Felix has co-authored over 30 publications and filed 6 patents. He received his Ph.D. from the University of British Columbia under the advisement of Professor Wolfgang Heidrich. He obtained his MSc from the University of Siegen, and was a postdoc at Stanford University. His doctoral dissertation won the Alain Fournier Ph.D. Dissertation Award and the SIGGRAPH outstanding doctoral dissertation award.	fheide@cs.princeton.edu	Felix Heide
20	NaN	gkol@cs.princeton.edu	Gillat Kol
21	Lecturer Iasonas Petras earned his doctorate in computer science from the Columbia University, where he also obtained a master’s in computer science. He also holds an M.Sc. in Mathematical Modeling in Modern Technologies and Economics from the National Technical University of Athens. His interests involve the algorithmic and complexity analysis of multivariate mathematical problems. He is researching quantum algorithms for continuous mathematical and physical problems that demonstrate a significant speedup compared to their classical counterparts. He also is studying ways to eliminate the "curse of dimensionality," the exponential dependence of the cost of algorithms on the dimension of the problem.	ipetras@cs.princeton.edu	Iasonas Petras
22	NaN	isma@cs.princeton.edu	Ibrahim Albluwi
23	NaN	jbrassil@cs.princeton.edu	Jack Brassil
24	Jaswinder Pal Singh joined the department in 1995 as an assistant professor, became an associate professor in 1999 and was appointed a full professor in 2005. From 2000 to 2005 he was co-founder and chief technical officer of FirstRain Inc., a business analytics company, where he led the development of novel and award-winning technologies and products for precise information extraction from Web pages in the presence of changes, for topic-specific crawling and information discovery, for high-relevance search, and for large-scale content-based publish-subscribe. Professor Singh received his bachelor’s degree from Princeton in 1987 and earned master’s and doctoral degrees in electrical engineering from Stanford in 1989 and 1993, respectively.  Since 2010, he has directed the Princeton CTO Program, which trains students to become highly effective chief technology officers by encouraging understanding not only of technology but also of business and society. Among his honors are the Presidential Early Career Award for Scientists and Engineers (PECASE), awarded by the National Science Foundation, and a Sloan research fellowship, both in 1997.  He is a member of the Association for Computing Machinery and the Institute of Electrical and Electronics Engineers Inc.	jps@cs.princeton.edu	Jaswinder Singh
25	Jennifer Rexford is the Gordon Y.S. Wu Professor of Engineering, and Chair of the Computer Science Department. Before joining Princeton in 2005, she worked for eight years at AT&T Labs—Research. She received her BSE in electrical engineering from Princeton in 1991, and her Ph.D. in electrical engineering and computer science from the University of Michigan in 1996. She served as the chair of ACM SIGCOMM from 2003 to 2007. Professor Rexford was the 2004 winner of ACM's Grace Murray Hopper Award for outstanding young computer professional. She is an ACM Fellow (2008) and a member of the American Academy of Arts and Sciences (2013) and the National Academy of Engineering (2014).	jrex@cs.princeton.edu	Jennifer Rexford
26	NaN	lumbroso@cs.princeton.edu	Jérémie Lumbroso
27	NaN	jiadeng@cs.princeton.edu	Jia Deng
28	Jonathan Mayer is an Assistant Professor at Princeton University, where he holds appointments in the Department of Computer Science and the Woodrow Wilson School of Public and International Affairs. Before joining the Princeton faculty, he served as the technology law and policy advisor to United States Senator Kamala Harris and as the Chief Technologist of the Federal Communications Commission Enforcement Bureau. Professor Mayer's research centers on the intersection of technology and law, with emphasis on national security, criminal procedure, and consumer privacy. He is both a computer scientist and a lawyer, and he holds a Ph.D. in computer science from Stanford University and a J.D. from Stanford Law School.	jrmayer@cs.princeton.edu	Jonathan Mayer
29	Kai Li, the Paul M. Wythes and Marcia R. Wythes Professor in Computer Science, earned a doctorate from Yale in 1986 and joined Princeton the same year. His research interests involve distributed and parallel systems, operating systems, storage systems, and content-based search of feature-rich data. In 2001, he co-founded Data Domain Inc., a provider of deduplication storage systems for efficient backup and data replication for disaster recovery. The company was acquired by EMC Corp. in 2009. Professor Li is an ACM fellow, IEEE fellow, a member of the National Academy of Engineering and the Washington State Academy of Sciences. In 2012, he won the ACM SIGOPS Hall of Fame Award and the Distinguished Achievement Award from the Chinese Institute of Engineers.	li@cs.princeton.edu	Kai Li
30	Karthik Narasimhan is an assistant professor in the Computer Science department at Princeton University. His research spans the areas of natural language processing and reinforcement learning, with a view towards building intelligent agents that learn to operate in the world through both experience and existing human knowledge (ex. text). He is especially interested in developing autonomous systems that can acquire language understanding through interaction with their environment while also utilizing textual knowledge to drive their decision making. Karthik received his PhD from MIT in 2017, and spent a year as a visiting research scientist at OpenAI prior to joining Princeton. His work has received a best paper award at EMNLP 2016 and an honorable mention for best paper at EMNLP 2015. 	 karthikn@cs.princeton.edu	Karthik Narasimhan
31	Kevin Wayne, the Phillip Y. Goldman Senior Lecturer in Computer Science, has been teaching at Princeton since 1998. He has codeveloped (with professor Robert Sedgewick) two of the most popular courses at Princeton: COS 126 (General Computer Science) and COS 226 (Algorithms and Data Structures), and two of the most popular MOOCs on the Coursera platform: Algorithms Part I and II. He has been named a Distinguished Educator by the ACM and has won several teaching awards at Princeton, including the SEAS Distinguished Teacher Award and the Phi Beta Kappa Teaching Award. He is a graduate of Yale University and received his master's and doctorate from Cornell University. His research interests include the design, analysis, and implementation of algorithms, especially for graphs and discrete optimization.	wayne@cs.princeton.edu	Kevin Wayne
32	Kyle Jamieson is an Associate Professor in the Department of Computer Science at Princeton University, where he has been on the faculty since 2015, after seven years on the faculty at University College London, U.K. Jamieson leads the Princeton Advanced Wireless Systems (PAWS) Group, whose charter is to build and experimentally evaluate wireless networking and wireless sensing systems for the real world that cut across the boundaries of digital communications, signal processing, and computer networking. He received the B.S. (2001), M.Eng. (2002), and Ph.D. (2008) degrees in Computer Science from the Massachusetts Institute of Technology. He then received a Starting Investigator fellowship from the European Research Council in 2011, Best Paper awards at USENIX 2013 and CoNEXT 2014, and a Google Faculty Research Award in 2015.	kylej@cs.princeton.edu	Kyle Jamieson
33	NaN	llp@cs.princeton.edu	Larry Peterson
34	NaN	maia@cs.princeton.edu	Maia Ginsburg
35	Margaret Martonosi is the Hugh Trumbull Adams '35 Professor of Computer Science at Princeton University, where she has been on the faculty since 1994. She is also Director of the Princeton’s Keller Center for Innovation in Engineering Education, and an A. D. White Visiting Professor-at-Large at Cornell University. From August 2015 through March, 2017, Martonosi was a Jefferson Science Fellow within the U.S. Department of State.\n\nMartonosi's research interests are in computer architecture and mobile computing. Her work has included the widely-used Wattch power modeling tool and the Princeton ZebraNet mobile sensor network project for the design and real-world deployment of zebra tracking collars in Kenya. Her current research focuses on computer architecture and hardware-software interface issues in both classical and quantum computing systems.\n\nMartonosi is a Fellow of IEEE and ACM. Her papers have received numerous long-term impact awards including: 2015 ISCA Long-Term Influential Paper Award, 2017 ACM SIGMOBILE Test-of-Time Award, 2017 ACM SenSys Test-of-Time Paper award, and the 2018 (Inaugural) HPCA Test-of-Time Paper award. Other notable awards include the 2018 IEEE Computer Society Technical Achievement Award, 2010 Princeton University Graduate Mentoring Award, the 2013 NCWIT Undergraduate Research Mentoring Award, the 2013 Anita Borg Institute Technical Leadership Award, and the 2015 Marie Pistilli Women in EDA Achievement Award. In addition to many archival publications, Martonosi is an inventor on seven granted US patents, and has co-authored two technical reference books on power-aware computer architecture. Martonosi completed her Ph.D. at Stanford University.	mrm@cs.princeton.edu	Margaret Martonosi
36	Professor Mark Braverman joined the department in 2011 from the University of Toronto, where he was an assistant professor in the mathematics and computer science departments. He earned his Ph.D. in 2008 from Toronto and did post-doctoral research at Microsoft Research New England, Cambridge, MA. Professor Braverman’s interests center on the connections between theoretical computer science and other disciplines, including information theory, mathematics, and economics. Most recently, he has been building new connections between information theory and complexity theory, studying the effects of noise in a variety of computational settings, and investigating how better algorithms can lead to better mechanism design, particularly in the context of healthcare.	mbraverm@cs.princeton.edu	Mark Braverman
37	NaN	mzhandry@cs.princeton.edu	Mark Zhandry
38	Before joining the faculty at Princeton, I spent two years as a postdoc in Princeton's CS Theory group, and was a research fellow at the Simons Institute during the Fall 2015 (Economics and Computation) and Fall 2016 (Algorithms and Uncertainty) semesters. I completed my PhD in 2014 at MIT, where I was very fortunate to be advised by Costis Daskalakis. Prior to that, I graduated from Cornell University with a BA in Math in 2010, where I was also fortunate to have worked with Bobby Kleinberg.	smattw@cs.princeton.edu	Matthew Weinberg
39	Michael J. Freedman is a Professor in the Computer Science Department at Princeton University, as well as the co-founder and CTO of Timescale, building an open-source database that scales out SQL for time-series data. His work broadly focuses on distributed systems, networking, and security. \n\nFreedman developed CoralCDN (a decentralized content distribution network serving millions of daily users) and Ethane (which formed the basis for the OpenFlow / software-defined networking architecture). He co-founded Illuminics Systems around IP geolocation and intelligence, which was acquired by Quova (now part of Neustar). Freedman is also a technical advisor to Blockstack, building a more decentralized Internet leveraging the blockchain. \n\nHonors include a Presidential Early Career Award for Scientists and Engineers (PECASE, given by President Obama), SIGCOMM Test of Time Award, Caspar Bowden Award for Privacy Enhancing Technologies, Sloan Fellowship, NSF CAREER Award, Office of Naval Research Young Investigator Award, DARPA Computer Science Study Group membership, and multiple award publications. Prior to joining Princeton in 2007, he received his Ph.D. in computer science from NYU's Courant Institute and his S.B. and M.Eng. degrees from MIT.	mfreed@cs.princeton.edu	Michael Freedman
57	Zachary Kincaid joined the department as an assistant professor in 2016.  He received his doctoral and master's degrees in computer science from the University of Toronto, and his bachelor's degree from Western University.  He is interested in programming languages, logic, and algorithms.  His research focuses on algorithms for reasoning about the behavior of software.	zkincaid@cs.princeton.edu	Zachary Kincaid
40	Mona Singh is a professor of computer science and the Lewis Sigler Institute for Integrative Genomics. She joined Princeton in 1999 as an assistant professor, became an associate professor in 2006 and was named a full professor in 2011.\n\nShe received her Ph.D. in computer science from MIT in 1996 after earning her master’s and bachelor’s degrees from Harvard. Her research interests involve developing and applying computational techniques to problems in molecular biology, with a focus on developing algorithms for genome-level analysis of protein structure and protein-protein interactions. She has been a member of the editorial board of the International Journal of Bioinformatics Research and Applications since 2004. Among her awards are the Presidential Early Career Award for Scientists and Engineers (PECASE) in 2001, and the Rheinstein Junior Faculty Award, from Princeton’s School of Engineering and Applied Science in 2003. 	mona@cs.princeton.edu	Mona Singh
41	Dr. Olga Russakovsky is an Assistant Professor in the Computer Science Department at Princeton University. Her research is in computer vision, closely integrated with machine learning and human-computer interaction. She completed her PhD at Stanford University and her postdoctoral fellowship at Carnegie Mellon University. She was awarded the PAMI Everingham Prize in 2016 as one of the leaders of the ImageNet Large Scale Visual Recognition Challenge, the MIT Technology Review's 35-under-35 Innovator award in 2017 and was named one of Foreign Policy Magazine's 100 Leading Global Thinkers in 2015. In addition to her research, she co-founded and continues to serve as a board member of the AI4ALL foundation dedicated to increasing diversity and inclusion in AI. She co-founded the Stanford AI4ALL camp teaching AI to high school girls (formerly "SAILORS") and the Princeton AI4ALL camp teaching AI to URM high school students.	olgarus@cs.princeton.edu	Olga Russakovsky
42	Olga G. Troyanskaya is a professor of computer science and the Lewis Sigler Institute for Integrative Genomics. She joined Princeton in 2003 as an assistant professor and became a full professor in 2013. She also is a consultant for the Simons Center for Data Analysis, in New York, and a visiting associate professor, Tromso University, Norway. Professor Troyanskaya received her doctorate in biomedical informatics from Stanford in 2003 and earned a bachelor’s in computer science and biology from the University of Richmond. Her professional service includes co-chair of an NHGRI workshop, “Integrating Functional Data for Connecting Genotype to Phenotype,” in 2012 and chair for the Late Breaking Research Track, Intelligent Systems for Molecular Biology (ISMB), also in 2012. She served on the steering committee for the ISMB/ECCB 2011 conference. Among her honors and awards are the 2014 Ira Herskowitz Award from the Genetic Society of America, the 2011 Overton Prize, from the International Society of Computational Biology, and the 2011 Blavatnik Award For Young Scientists (Finalist Award).	ogt@cs.princeton.edu	Olga Troyanskaya
43	NaN	ranr@cs.princeton.edu	Ran Raz
44	Robert Dondero is a Lecturer in Computer Science.  Prior to arriving at Princeton in 2001 he was a professional programmer in industry, a tenured assistant professor at La Salle University, and an adjunct professor at The Pennsylvania State University.  He earned his Ph.D. at Drexel University in 2008.  At Princeton his primary responsibility is teaching the COS 217 course.  For his work on that course his students have chosen him to receive eight Engineering Council Excellence in Engineering Education awards, and the Engineering Council Lifetime Achievement Award for Excellence in Teaching.	rdondero@cs.princeton.edu	Robert Dondero
45	Besides his activities at Princeton, Dr. Fish is President of NETovations, LLC, a consulting company focused on the creation of communications and networking technology innovation and standardization. From 2007 to 2010, he was Chief Product Officer and Senior VP at Mformation, Inc. specializing in carrier software for mobile device management. From 1997 to 2007, Rob was Vice President and Managing Director of Panasonic US R&D laboratories working on the embedding of networking in consumer devices. Prior to this, he was Executive Director, Multimedia Communications Research at Bell Communications Research (Bellcore) after starting his career at Bell Laboratories. \n\nRob is the President of the IEEE Standards Association and a member of the Board of Directors of the IEEE.  He is also a member of the Board of Governors of the IEEE Communications Society.  He co-edited a series in IEEE Communications Magazine on IEEE standards in communications and networking. He is Co-founder and formerly the Steering Committee Chair of IEEE ComSoc’s Consumer Communications and Networking Conference. For his leadership and contributions to the Multimedia Communications Technical Committee, Dr. Fish was the recipient of MMTC’s Distinguished Service Award.  Rob was also awarded the the Standards Medallion of the IEEE Standards Association.   Dr. Fish was elected as a Fellow of the IEEE "for application of visual communications and networking." \n\nRob’s interests are pretty wide ranging. They include networking and telecom; learning, perception, and intelligence, artificial and otherwise; Human-Computer interaction and Computer-Supported Collaborative Work; as well as the general topic of R&D innovation methodologies and entrepreneurial applications of those methodologies.	rfish@cs.princeton.edu	Robert Fish
46	Robert Schapire is a Principal Researcher at Microsoft Research in New York City, and is currently a Visiting Lecturer in Computer Science. He received his PhD from MIT in 1991. After a short post-doc at Harvard, he joined the technical staff at AT&T Labs (formerly AT&T Bell Laboratories) in 1991. In 2002, he became a Professor of Computer Science at Princeton University. He joined Microsoft Research in 2014. His awards include the 1991 ACM Doctoral Dissertation Award, the 2003 Gödel Prize, and the 2004 Kanelakkis Theory and Practice Award (both of the last two with Yoav Freund). He is a fellow of the AAAI, and a member of both the National Academy of Engineering and the National Academy of Sciences. His main research interest is in theoretical and applied machine learning, with particular focus on boosting, online learning, game theory, and maximum entropy.	schapire@cs.princeton.edu	Robert Schapire
58	Zeev Dvir, an assistant professor in the computer science and mathematics departments, received his Ph.D. in 2008 from the Weizmann Institute of Science in Rehovot, Israel, and did post-doctoral work at the Institute for Advanced Study. He has a broad interest in theoretical computer science and mathematics, with special attention to computational complexity, pseudo-randomness, coding theory and discrete geometry. He was awarded an Alfred P. Sloan Foundation Research Fellowship in 2013. In 2012, he won the Dénes König award from the SIAM Conference on Discrete Mathematics, and in 2011 was awarded the Alfred Rheinstein ’11 award, given each year to an assistant professor in the School of Engineering who has shown exceptional promise.	zdvir@cs.princeton.edu	Zeev Dvir
47	Robert Sedgewick, the William O. Baker Professor in Computer Science, in 1985 was the founding chair of the Department of Computer Science, a position he held until 1994. Before joining Princeton, he was a professor for 10 years at Brown University, where he earned bachelor’s and master’s degrees in applied mathematics. He received his Ph.D. in computer science from Stanford in 1975. Professor Sedgewick’s research interests revolve around algorithm design, including mathematical techniques for the analysis of algorithms. He has published widely in these areas and is the author of 16 books, including a well-known series of textbooks on algorithms that have sold more than one-half million copies and (with P. Flajolet) a research monograph on analytic combinatorics that defines the field. He has held visiting research positions at Xerox PARC in Palo Alto, CA; the Institute for Defense Analyses in Princeton; and Inria in Rocquencourt, France, and has been a member of the board of directors of Adobe Systems since 1990. He chairs steering committees that organize conferences on analytic combinatorics, analysis of algorithms, and data structures throughout the world. With Kevin Wayne, he has developed four MOOCs (which have attracted over one million registrants) and extensive associated online conten (which attracts millions of page visits per year).	rs@cs.princeton.edu	Robert Sedgewick
48	Robert E. Tarjan, the James S. McDonnell Distinguished University Professor of Computer Science, joined Princeton in 1985. He received doctoral and master’s degrees in computer science from Stanford in 1972 and 1971, respectively, after earning a bachelor’s in mathematics from Caltech. His academic experience involved assistant professorships at Cornell and Stanford, and a Miller research fellowship at UC, Berkeley. Professor Tarjan’s extensive involvement in the private sector includes past and continuing fellowship, research and scientific roles at the NEC Research Institute, Princeton; InterTrust Technologies, Sunnyvale, CA; Compaq Computer, Houston, TX; Hewlett-Packard, Palo Alto, CA; and Microsoft, Mountain View, CA. His honors include Caltech’s Distinguished Alumni Award in 2010, the 2009 Edelman Award from INFORMS (member of winning H-P team), fellow of the Society for Industrial and Applied Mathematics (2009), and the Blaise Pascal Medal in Mathematics and Computer Science from the European Academy of Sciences in 2004. Professor Tarjan was the first winner of the Rolf Nevanlinna Prize, established in 1982 and awarded every four years for outstanding contributions in mathematical aspects of information sciences by the International Mathematical Union.	ret@cs.princeton.edu	Robert Tarjan
49	I am the director of the Undergraduate Certificate in Statistics and Machine Learning. I co-founded Whetlab (sold to Twitter in 2015) and formerly co-hosted the Talking Machines podcast. I was faculty at Harvard from 2011 to 2016 and was at Twitter and then Google Brain before joining the faculty at Princeton in 2018. I call my group the Laboratory for Intelligent Probabilistic Systems (LIPS).	rpa@cs.princeton.edu	Ryan Adams
50	Sanjeev Arora is the Charles C. Fitzmorris Professor in Computer Science. He joined Princeton in 1994 after earning his doctorate from the University of California, Berkeley. He was a visiting professor at the Weizmann Institute in 2007, a visiting researcher at Microsoft in 2006-07, and a visiting associate professor at Berkeley during 2001-02. Professor Arora’s honors include the D.R. Fulkerson Prize in Discrete Mathematics (awarded by the American Mathematical Society and Math Optimization Society) in 2012, the ACM-Infosys Foundation Award in the Computing Sciences in the same year, the Best paper award from IEEE Foundations of Computer Science in 2010, and the EATCS-SIGACT Gödel Prize (cowinner), also in 2010. He was appointed a Simons Foundation investigator in 2012, and was elected an ACM fellow in 2009. Professor Arora was the founding director and lead PI at the Center for Computational Intractability in 2008, a project funded partly by an NSF Expeditions in Computing grant.	arora@cs.princeton.edu	Sanjeev Arora
51	Sebastian Seung is Professor at the Princeton Neuroscience Institute and Department of Computer Science. Seung has done influential research in both computer science and neuroscience. Over the past decade, he helped pioneer the new field of connectomics, developing machine learning and social computing technologies for reconstructing neural circuits from high resolution brain images. His lab created EyeWire, a site that has recruited over 150,000 players from 130 countries to a game to map neural connections.\nSeung is also known for his efforts to communicate neuroscience to the general public. His TED Talk "I am my connectome" has more than 750,000 views, and has been translated into 26 languages. His book Connectome: How the Brain's Wiring Makes Us Who We Are was chosen by the Wall Street Journal as Top Ten Nonfiction of 2012.\nBefore joining the Princeton faculty in 2014, Seung studied at Harvard University, worked at Bell Laboratories, and taught at the Massachusetts Institute of Technology. He is an External Member of the Max Planck Society, and winner of the 2008 Ho-Am Prize in Engineering.	sseung@cs.princeton.edu	Sebastian Seung
52	Szymon Rusinkiewicz is Professor of Computer Science at Princeton University.  His work focuses on the interface between computers and the visual and tangible world: acquisition, representation, analysis, and fabrication of 3D shape, motion, surface appearance, and scattering. He investigates algorithms for processing geometry and reflectance, including registration, matching, completion, hierarchical decomposition, symmetry analysis, sampling, and depiction.  Applications of this work include documentation of cultural heritage artifacts and sites, appearance and performance capture for digital humans, and illustrative depiction through line drawings and non-photorealistic shading models.	smr@cs.princeton.edu	Szymon Rusinkiewicz
53	People solve challenging computational problems every day, making predictions about future events, learning new causal relationships, or discovering how objects should be divided into categories. My research investigates how this is possible, first identifying the nature of the underlying computational problems, and then examining whether we can explain aspects of human behavior as the result of approximating optimal solutions to those problems. Since many of the problems people face in everyday life are problems of induction, requiring inferences from limited data to underconstrained hypotheses, these optimal solutions draw on methods developed in statistics, machine learning, and artificial intelligence research. Exploring how these methods relate to human cognition provides connections between these fields and cognitive science, as well as a way to turn insights obtained from studying people into new formal techniques.	tomg@cs.princeton.edu	Tom Griffiths
54	Wyatt Lloyd is an Assistant Professor of Computer Science. His research interests include the distributed systems and networking problems that underlie the architecture of large-scale Web sites, cloud computing, and big data. He received his Ph.D. from Princeton University in 2013, spend the next year as a Postdoctoral Researcher at Facebook, and spent 3 years as an Assistant Professor of Computer Science at the University of Southern California before returning to Princeton in 2017.	wlloyd@cs.princeton.edu	Wyatt Lloyd
\.


--
-- Data for Name: projects; Type: TABLE DATA; Schema: public; Owner: ptaylor
--

COPY public.projects (title, description, prof_id) FROM stdin;
sylver: synthesis	\N	0
learning	\N	0
and verification	\N	0
3d shape-based retrieval and analysis	\N	1
decobrush: drawing structured decorative patterns by example	\N	1
painting with triangles	\N	1
realpigment: paint compositing by example	\N	1
stylized keyframe animation of fluid simulations	\N	1
3d content creation made easy through non-photorealism	\N	1
illustration and analysis of images with normals	\N	1
suggestive contours	\N	1
certicoq: principled optimizing compilation of dependently typed programs	\N	4
verified software toolchain	\N	4
concurrent c minor	\N	4
foundational proof-carrying code	\N	4
proof-carrying authorization	\N	4
standard ml of new jersey	\N	4
big data: anonymity	\N	5
privacy	\N	5
ethics	\N	5
bitcoin and cryptocurrencies	\N	5
web privacy	\N	5
epigenome-wide association studies	\N	6
population structure and matrix factorization	\N	6
protein molecular function prediction	\N	6
statistical analysis of genetic association studies	\N	6
understanding how eqtls work by looking across eqtl studies	\N	6
cell types	\N	6
and regulatory element data	\N	6
natural algorithms	\N	7
wordnet	\N	9
liberty research	\N	13
structural modeling	\N	13
thrift	\N	13
velocity compiler	\N	13
3d shape-based retrieval and analysis	\N	14
frenetic	\N	15
pads	\N	15
polymer - a language for composing run-time security policies	\N	15
typed assembly language (tal)	\N	15
zap	\N	15
proof-carrying authorization	\N	17
secure applications for handheld devices	\N	17
learning with partial feedback	\N	18
online convex optimization	\N	18
projection free learning	\N	18
sublinear optimization	\N	18
enterprise and data-center networks	\N	25
internet architecture	\N	25
internet policy	\N	25
software-defined networking	\N	25
cass: content-aware search system	\N	29
fcma: full correlation matrix analysis of human	\N	29
brains	\N	29
imagenet	\N	29
parsec	\N	29
seek: search engine for heterogeneous human gene-expression compendia	\N	29
princeton advanced wireless systems (paws) group	\N	32
planetlab	\N	33
syndicate	\N	33
prof. martonosi computer architecture research	\N	35
frenetic	\N	39
geo-replicated cloud storage	\N	39
least-privilege web services	\N	39
princeton s* network systems (sns) group	\N	39
resource allocation for cloud services	\N	39
service-centric networking	\N	39
untrusted cloud services	\N	39
computational molecular biology	\N	40
bioinformatics & functional genomics	\N	42
cass: content-aware search system	\N	42
biological process inference from experimental interaction evidence (biopixie)	\N	42
boosting	\N	46
computational neuroscience	\N	51
eyewire	\N	51
3d shape-based retrieval and analysis	\N	52
illustration and analysis of images with normals	\N	52
measurement and representation of realistic surface appearance	\N	52
new techniques for range scanning	\N	52
qsplat	\N	52
reassembling the thera wall paintings	\N	52
suggestive contours	\N	52
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: ptaylor
--

COPY public.users (username, password) FROM stdin;
\.


--
-- Name: areas_prof_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ptaylor
--

SELECT pg_catalog.setval('public.areas_prof_id_seq', 1, false);


--
-- Name: profs_prof_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ptaylor
--

SELECT pg_catalog.setval('public.profs_prof_id_seq', 1, false);


--
-- Name: projects_prof_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ptaylor
--

SELECT pg_catalog.setval('public.projects_prof_id_seq', 1, false);


--
-- Name: profs profs_pkey; Type: CONSTRAINT; Schema: public; Owner: ptaylor
--

ALTER TABLE ONLY public.profs
    ADD CONSTRAINT profs_pkey PRIMARY KEY (prof_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: ptaylor
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (username);


--
-- Name: areas areas_prof_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ptaylor
--

ALTER TABLE ONLY public.areas
    ADD CONSTRAINT areas_prof_id_fkey FOREIGN KEY (prof_id) REFERENCES public.profs(prof_id);


--
-- Name: projects projects_prof_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: ptaylor
--

ALTER TABLE ONLY public.projects
    ADD CONSTRAINT projects_prof_id_fkey FOREIGN KEY (prof_id) REFERENCES public.profs(prof_id);


--
-- PostgreSQL database dump complete
--

