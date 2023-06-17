import streamlit as st
import itertools
from itertools import groupby

# Fungsi untuk menampilkan data agama
import pandas as pd

def display_data(data, provinsi):
    agama_data = group_by_agama(data, provinsi)
    df = pd.DataFrame(list(agama_data.items()), columns=['Agama', 'Jumlah Pemeluk'])


def display_data():

    provinsi_data = group_by_provinsi(data)
    agama_data = group_by_agama(data)
                    

# Data yang akan ditampilkan
data = [
    {'provinsi':	'Aceh',     'agama': 'Islam       ',    'jumlah_pemeluk'	:	5271485 	},
    {'provinsi':	'Aceh',  	'agama': 'kristen     ',    'jumlah_pemeluk'	:	63486		},
    {'provinsi':	'Aceh',  	'agama': 'katolik     ',    'jumlah_pemeluk'	:	5511 		},		
    {'provinsi':	'Aceh',  	'agama': 'hindu       ',    'jumlah_pemeluk'	:	95		    },
    {'provinsi':	'Aceh',  	'agama': 'budha       ',    'jumlah_pemeluk'	:	7045		},		
    {'provinsi':	'Aceh',  	'agama': 'konghucu    ',    'jumlah_pemeluk'	:	1		    },	
    {'provinsi':	'Aceh',  	'agama': 'lainnya     ',    'jumlah_pemeluk'	:	264		    },	

    {'provinsi': 	'Sumatera Utara',       'agama': 'Islam       ',    'jumlah_pemeluk'   : 	10124754	},
    {'provinsi': 	'Sumatera Utara',       'agama': 'Katholik    ',    'jumlah_pemeluk'   : 	4085380	    },
    {'provinsi': 	'Sumatera Utara',       'agama': 'Kristen     ',    'jumlah_pemeluk'   : 	654764      },
    {'provinsi': 	'Sumatera Utara',       'agama': 'Buddha      ',    'jumlah_pemeluk'   : 	16091       },
    {'provinsi': 	'Sumatera Utara',       'agama': 'Hindu       ',    'jumlah_pemeluk'   : 	3554477     },
    {'provinsi': 	'Sumatera Utara',       'agama': 'Konghucu    ',    'jumlah_pemeluk'   : 	770         },
    {'provinsi': 	'Sumatera Utara',       'agama': 'Lainnya     ',    'jumlah_pemeluk'   : 	5084        },

    {'provinsi':	'Sumatera Barat',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	5470109	    },
    {'provinsi':	'Sumatera Barat',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	83794		},
    {'provinsi':	'Sumatera Barat',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	46773		},
    {'provinsi':	'Sumatera Barat',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	95		    },
    {'provinsi':	'Sumatera Barat',		'agama': 'budha       ',    'jumlah_pemeluk'	:	3415		},
    {'provinsi':	'Sumatera Barat',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	5		    },
    {'provinsi':	'Sumatera Barat',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	265         },

    {'provinsi':	'Sumatera Selatan',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	8324093	    },
    {'provinsi':	'Sumatera Selatan',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	82875		},
    {'provinsi':	'Sumatera Selatan',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	49954		},
    {'provinsi':	'Sumatera Selatan',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	41121		},
    {'provinsi':	'Sumatera Selatan',		'agama': 'budha       ',    'jumlah_pemeluk'	:	67588		},
    {'provinsi':	'Sumatera Selatan',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	97		    },
    {'provinsi':	'Sumatera Selatan',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	70		    },	
	
    {'provinsi':	'Riau',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	5726306	    },
    {'provinsi':	'Riau',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	638119	    },
    {'provinsi':	'Riau',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	69867		},
    {'provinsi':	'Riau',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	767		    },
    {'provinsi':	'Riau',		'agama': 'budha       ',    'jumlah_pemeluk'	:	136542	    },
    {'provinsi':	'Riau',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	2204		},
    {'provinsi':	'Riau',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	1126		},


    {'provinsi':	'Jambi',	'agama': 'Islam       ',    'jumlah_pemeluk'	:	3425742	    },
    {'provinsi':	'Jambi',	'agama': 'kristen     ',    'jumlah_pemeluk'	:	119044	    },
    {'provinsi':	'Jambi',	'agama': 'katolik     ',    'jumlah_pemeluk'	:	2094		},
    {'provinsi':	'Jambi',	'agama': 'hindu       ',    'jumlah_pemeluk'	:	488		    },
    {'provinsi':	'Jambi',	'agama': 'budha       ',    'jumlah_pemeluk'	:	34293		},
    {'provinsi':	'Jambi',	'agama': 'konghucu    ',    'jumlah_pemeluk'	:	791		    },
    {'provinsi':	'Jambi',    'agama': 'lainnya     ',    'jumlah_pemeluk'	:	2126		},
	
    {'provinsi':	'Bengkulu',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	1989720	    },
    {'provinsi':	'Bengkulu',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	32935		},
    {'provinsi':	'Bengkulu',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	8038		},
    {'provinsi':	'Bengkulu',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	4138		},
    {'provinsi':	'Bengkulu',		'agama': 'budha       ',    'jumlah_pemeluk'	:	2082		},
    {'provinsi':	'Bengkulu',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	11		    },
    {'provinsi':	'Bengkulu',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	95		    },

    {'provinsi':	'Lampung',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	8531111	    },
    {'provinsi':	'Lampung',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	122692	    },
    {'provinsi':	'Lampung',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	77755		},
    {'provinsi':	'Lampung',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	1251		},
    {'provinsi':	'Lampung',		'agama': 'budha       ',    'jumlah_pemeluk'	:	24507		},
    {'provinsi':	'Lampung',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	129		    },
    {'provinsi':	'Lampung',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	807		    },
	
    {'provinsi':	'Kep. Bangka Belitung',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	1316560	    },
    {'provinsi':	'Kep. Bangka Belitung',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	30755		},
    {'provinsi':	'Kep. Bangka Belitung',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	19058		},
    {'provinsi':	'Kep. Bangka Belitung',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	1225		},
    {'provinsi':	'Kep. Bangka Belitung',		'agama': 'budha       ',    'jumlah_pemeluk'	:	63778		},
    {'provinsi':	'Kep. Bangka Belitung',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	29378		},
    {'provinsi':	'Kep. Bangka Belitung',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	1138		},
	
    {'provinsi': 	'Riau',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	1631245	    },
    {'provinsi': 	'Riau',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	248235	    },
    {'provinsi': 	'Riau',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	52191		},
    {'provinsi': 	'Riau',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	927		    },
    {'provinsi': 	'Riau',		'agama': 'budha       ',    'jumlah_pemeluk'	:	146626	    },
    {'provinsi': 	'Riau',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	3254		},
    {'provinsi': 	'Riau',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	307		    },

    {'provinsi':	'Jakarta',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	9442139	    },
    {'provinsi':	'Jakarta',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	963715	    },
    {'provinsi':	'Jakarta',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	437996	    },
    {'provinsi':	'Jakarta',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	20413		},
    {'provinsi':	'Jakarta',		'agama': 'budha       ',    'jumlah_pemeluk'	:	395365	    },
    {'provinsi':	'Jakarta',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	1698		},
    {'provinsi':	'Jakarta', 		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	269		    },
		
    {'provinsi':	'Jawa Barat',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	46923543	},
    {'provinsi':	'Jawa Barat',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	865382	    },
    {'provinsi':	'Jawa Barat',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	29989		},
    {'provinsi':	'Jawa Barat',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	17082		},
    {'provinsi':	'Jawa Barat',		'agama': 'budha       ',    'jumlah_pemeluk'	:	98753		},
    {'provinsi':	'Jawa Barat',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	12111		},
    {'provinsi':	'Jawa Barat',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	3282		},
		
    {'provinsi':	'Jawa Tengah',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	36296971	},
    {'provinsi':	'Jawa Tengah',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	594871	    },
    {'provinsi':	'Jawa Tengah',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	347772	    },
    {'provinsi':	'Jawa Tengah',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	14618		},
    {'provinsi':	'Jawa Tengah',		'agama': 'budha       ',    'jumlah_pemeluk'	:	51276		},
    {'provinsi':	'Jawa Tengah',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	1344		},
    {'provinsi':	'Jawa Tengah',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	6204		},

    {'provinsi':	'Jawa Timur',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	39925335	},
    {'provinsi':	'Jawa Timur',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	681474	    },
    {'provinsi':	'Jawa Timur',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	275735	    },
    {'provinsi':	'Jawa Timur',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	104987	    },
    {'provinsi':	'Jawa Timur',		'agama': 'budha       ',    'jumlah_pemeluk'	:	71198		},
    {'provinsi':	'Jawa Timur',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	2065		},
    {'provinsi':	'Jawa Timur',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	2294		},

    {'provinsi':	'Yogyakarta',	    'agama': 'Islam       ',    'jumlah_pemeluk'	:	3415882	    },
    {'provinsi':	'Yogyakarta',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	89454		},
    {'provinsi':	'Yogyakarta',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	165191	    },
    {'provinsi':	'Yogyakarta',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	3421		},
    {'provinsi':	'Yogyakarta',		'agama': 'budha       ',    'jumlah_pemeluk'	:	307		    },
    {'provinsi':	'Yogyakarta',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	72		    },
    {'provinsi':	'Yogyakarta',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	356		    },
		
    {'provinsi':	'Banten',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	11410170	},
    {'provinsi':	'Banten',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	314182	    },
    {'provinsi':	'Banten',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	145206	    },
    {'provinsi':	'Banten',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	8566		},
    {'provinsi':	'Banten',		'agama': 'budha       ',    'jumlah_pemeluk'	:	1429		},
    {'provinsi':	'Banten',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	2267		},
    {'provinsi':	'Banten',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	759		    },
		
    {'provinsi':	'Bali',			'agama': 'Islam       ',    'jumlah_pemeluk'	:	430924	    },
    {'provinsi':	'Bali',			'agama': 'kristen     ',    'jumlah_pemeluk'	:	69602		},
    {'provinsi':	'Bali',			'agama': 'katolik     ',    'jumlah_pemeluk'	:	34852		},
    {'provinsi':	'Bali',			'agama': 'hindu       ',    'jumlah_pemeluk'	:	3714068	    },
    {'provinsi':	'Bali',			'agama': 'budha       ',    'jumlah_pemeluk'	:	29023		},
    {'provinsi':	'Bali',			'agama': 'konghucu    ',    'jumlah_pemeluk'	:	560		    },
    {'provinsi':	'Bali',			'agama': 'lainnya     ',    'jumlah_pemeluk'	:	97		    },
	
    {'provinsi':	'Nusa Tenggara Barat',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	5260683	    },
    {'provinsi':	'Nusa Tenggara Barat',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	13539		},
    {'provinsi':	'Nusa Tenggara Barat',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	10021		},
    {'provinsi':	'Nusa Tenggara Barat',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	130966	    },
    {'provinsi':	'Nusa Tenggara Barat',		'agama': 'budha       ',    'jumlah_pemeluk'	:	16911		},
    {'provinsi':	'Nusa Tenggara Barat',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	44		    },
    {'provinsi':	'Nusa Tenggara Barat',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	43		    },
	
    {'provinsi':	'Nusa Tenggara Timur',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	518916	    },
    {'provinsi':	'Nusa Tenggara Timur',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	1987688	    },
    {'provinsi':	'Nusa Tenggara Timur',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	2941807	    },
    {'provinsi':	'Nusa Tenggara Timur',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	5803		},
    {'provinsi':	'Nusa Tenggara Timur',		'agama': 'budha       ',    'jumlah_pemeluk'	:	378		    },
    {'provinsi':	'Nusa Tenggara Timur',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	24		    },
    {'provinsi':	'Nusa Tenggara Timur',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	35229		},
	
    {'provinsi':	'Kalimantan Barat',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	3290832	    },
    {'provinsi':	'Kalimantan Barat',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	633174	    },
    {'provinsi':	'Kalimantan Barat',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	1210295	    },
    {'provinsi':	'Kalimantan Barat',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	2788		},
    {'provinsi':	'Kalimantan Barat',		'agama': 'budha       ',    'jumlah_pemeluk'	:	313504	    },
    {'provinsi':	'Kalimantan Barat', 	'agama': 'konghucu    ',    'jumlah_pemeluk'	:	15095		},
    {'provinsi':	'Kalimantan Barat',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	122		    },

    {'provinsi':	'Kalimantan Tengah',	'agama': 'Islam       ',    'jumlah_pemeluk'	:	1970660	    },
    {'provinsi':	'Kalimantan Tengah',	'agama': 'kristen     ',    'jumlah_pemeluk'	:	44305		},
    {'provinsi':	'Kalimantan Tengah',	'agama': 'katolik     ',    'jumlah_pemeluk'	:	87325		},
    {'provinsi':	'Kalimantan Tengah',	'agama': 'hindu       ',    'jumlah_pemeluk'	:	151445	    },
    {'provinsi':	'Kalimantan Tengah',	'agama': 'budha       ',    'jumlah_pemeluk'	:	287		    },
    {'provinsi':	'Kalimantan Tengah',	'agama': 'konghucu    ',    'jumlah_pemeluk'	:	178		    },
    {'provinsi':	'Kalimantan Tengah',	'agama': 'lainnya     ',    'jumlah_pemeluk'	:	856		    },

    {'provinsi':	'Kalimantan Selatan',	'agama': 'Islam       ',    'jumlah_pemeluk'	:	3996958	    },
    {'provinsi':	'Kalimantan Selatan',	'agama': 'kristen     ',    'jumlah_pemeluk'	:	55005		},
    {'provinsi':	'Kalimantan Selatan',	'agama': 'katolik     ',    'jumlah_pemeluk'	:	22523		},
    {'provinsi':	'Kalimantan Selatan',	'agama': 'hindu       ',    'jumlah_pemeluk'	:	23823		},
    {'provinsi':	'Kalimantan Selatan',	'agama': 'budha       ',    'jumlah_pemeluk'	:	12185		},
    {'provinsi':	'Kalimantan Selatan',	'agama': 'konghucu    ',    'jumlah_pemeluk'	:	202		    },
    {'provinsi':	'Kalimantan Selatan',	'agama': 'lainnya     ',    'jumlah_pemeluk'	:	9121		},
	
    {'provinsi':	'Kalimantan Timur',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	3365718	    },
    {'provinsi':	'Kalimantan Timur',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	288806	    },
    {'provinsi':	'Kalimantan Timur',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	170453	    },
    {'provinsi':	'Kalimantan Timur',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	8552		},
    {'provinsi':	'Kalimantan Timur',		'agama': 'budha       ',    'jumlah_pemeluk'	:	15648		},
    {'provinsi':	'Kalimantan Timur',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	345		    },
    {'provinsi':	'Kalimantan Timur',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	297		    },
		
    {'provinsi':	'Kalimantan Utara',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	511874	    },
    {'provinsi':	'Kalimantan Utara',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	138437	    },
    {'provinsi':	'Kalimantan Utara',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	43064		},
    {'provinsi':	'Kalimantan Utara',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	337		    },
    {'provinsi':	'Kalimantan Utara',		'agama': 'budha       ',    'jumlah_pemeluk'	:	4122		},
    {'provinsi':	'Kalimantan Utara',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	148		    },
    {'provinsi':	'Kalimantan Utara',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	14		    },

    {'provinsi':	'Sulawesi Utara',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	845194	    },
    {'provinsi':	'Sulawesi Utara',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	1672955	    },
    {'provinsi':	'Sulawesi Utara',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	118108	    },
    {'provinsi':	'Sulawesi Utara',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	15793		},
    {'provinsi':	'Sulawesi Utara',		'agama': 'budha       ',    'jumlah_pemeluk'	:	3869		},
    {'provinsi':	'Sulawesi Utara',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	428		    },
    {'provinsi':	'Sulawesi Utara',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	1647		},
	
    {'provinsi':	'Sulawesi Tengah',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	2408937	    },
    {'provinsi':	'Sulawesi Tengah',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	496912	    },
    {'provinsi':	'Sulawesi Tengah',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	27523		},
    {'provinsi':	'Sulawesi Tengah',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	11087		},
    {'provinsi':	'Sulawesi Tengah',		'agama': 'budha       ',    'jumlah_pemeluk'	:	4222		},
    {'provinsi':	'Sulawesi Tengah',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	27		    },
    {'provinsi':	'Sulawesi Tengah',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	3261		},
		
    {'provinsi':	'Sulawesi Selatan',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	8263575 	},
    {'provinsi':	'Sulawesi Selatan',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	692908	    },
    {'provinsi':	'Sulawesi Selatan',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	152282	    },
    {'provinsi':	'Sulawesi Selatan',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	63499		},
    {'provinsi':	'Sulawesi Selatan',		'agama': 'budha       ',    'jumlah_pemeluk'	:	20636		},
    {'provinsi':	'Sulawesi Selatan',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	76		    },
    {'provinsi':	'Sulawesi Selatan',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	25758		},
	
    {'provinsi':	'Sulawesi Tenggara',	'agama': 'Islam       ',    'jumlah_pemeluk'	:	2565710	    },
    {'provinsi':	'Sulawesi Tenggara',	'agama': 'kristen     ',    'jumlah_pemeluk'	:	44795		},
    {'provinsi':	'Sulawesi Tenggara',	'agama': 'katolik     ',    'jumlah_pemeluk'	:	16215		},
    {'provinsi':	'Sulawesi Tenggara',	'agama': 'hindu       ',    'jumlah_pemeluk'	:	50814		},
    {'provinsi':	'Sulawesi Tenggara',	'agama': 'budha       ',    'jumlah_pemeluk'	:	1528		},
    {'provinsi':	'Sulawesi Tenggara',	'agama': 'konghucu    ',    'jumlah_pemeluk'	:	15		    },
    {'provinsi':	'Sulawesi Tenggara',	'agama': 'lainnya     ',    'jumlah_pemeluk'	:	56		    },
		
    {'provinsi':	'Sulawesi Barat',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	1208735	    },
    {'provinsi':	'Sulawesi Barat',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	192483	    },
    {'provinsi':	'Sulawesi Barat',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	15652	    },
    {'provinsi':	'Sulawesi Barat',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	1951	    },
    {'provinsi':	'Sulawesi Barat',		'agama': 'budha       ',    'jumlah_pemeluk'	:	419		    },
    {'provinsi':	'Sulawesi Barat',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	6		    },
    {'provinsi':	'Sulawesi Barat',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	542		    },

    {'provinsi':	'Gorontalo',	    'agama': 'Islam       ',    'jumlah_pemeluk'	:	1176947	    },
    {'provinsi':	'Gorontalo',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	17517		},
    {'provinsi':	'Gorontalo',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	1114		},
    {'provinsi':	'Gorontalo',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	4115		},
    {'provinsi':	'Gorontalo',		'agama': 'budha       ',    'jumlah_pemeluk'	:	945		    },
    {'provinsi':	'Gorontalo',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	5		    },
    {'provinsi':	'Gorontalo',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	20		    },
		
    {'provinsi':	'Maluku',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	991664	    },
    {'provinsi':	'Maluku',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	743412	    },
    {'provinsi':	'Maluku',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	129179	    },
    {'provinsi':	'Maluku',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	6601		},
    {'provinsi':	'Maluku',		'agama': 'budha       ',    'jumlah_pemeluk'	:	366		    },
    {'provinsi':	'Maluku',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	63		    },
    {'provinsi':	'Maluku',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	9378		},

    {'provinsi':	'Maluku Utara',		'agama': 'Islam       ',    'jumlah_pemeluk'	:	986743	    },
    {'provinsi':	'Maluku Utara',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	330052	    },
    {'provinsi':	'Maluku Utara',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	6749		},
    {'provinsi':	'Maluku Utara',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	114		    },
    {'provinsi':	'Maluku Utara',		'agama': 'budha       ',    'jumlah_pemeluk'	:	134		    },
    {'provinsi':	'Maluku Utara',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	127		    },
    {'provinsi':	'Maluku Utara',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	8		    },
		
    {'provinsi':	'Papua',	'agama': 'Islam       ',    'jumlah_pemeluk'	:	627581	    },
    {'provinsi':	'Papua',	'agama': 'kristen     ',    'jumlah_pemeluk'	:	2995059	    },
    {'provinsi':	'Papua',	'agama': 'katolik     ',    'jumlah_pemeluk'	:	675154	    },
    {'provinsi':	'Papua',	'agama': 'hindu       ',    'jumlah_pemeluk'	:	3139		},
    {'provinsi':	'Papua',	'agama': 'budha       ',    'jumlah_pemeluk'	:	2068		},
    {'provinsi':	'Papua',	'agama': 'konghucu    ',    'jumlah_pemeluk'	:	74		    },
    {'provinsi':	'Papua',	'agama': 'lainnya     ',    'jumlah_pemeluk'	:	2759		},
		
    {'provinsi':	'Papua Barat', 		'agama': 'Islam       ',    'jumlah_pemeluk'	:	438841	    },
    {'provinsi':	'Papua Barat',		'agama': 'kristen     ',    'jumlah_pemeluk'	:	619802	    },
    {'provinsi':	'Papua Barat',		'agama': 'katolik     ',    'jumlah_pemeluk'	:	89441		},
    {'provinsi':	'Papua Barat',		'agama': 'hindu       ',    'jumlah_pemeluk'	:	1189		},
    {'provinsi':	'Papua Barat',		'agama': 'budha       ',    'jumlah_pemeluk'	:	895		    },
    {'provinsi':	'Papua Barat',		'agama': 'konghucu    ',    'jumlah_pemeluk'	:	21		    },
    {'provinsi':	'Papua Barat',		'agama': 'lainnya     ',    'jumlah_pemeluk'	:	54		    },
]

# Fungsi untuk mengelompokkan data berdasarkan provinsi
def group_by_provinsi(data):
    return {
        provinsi: list(agama)
        for provinsi, agama in itertools.groupby(data, key=lambda x: x['provinsi'])
    } 

# Fungsi untuk mengelompokkan data pemeluk berdasarkan agama
def group_by_agama(data, provinsi=None):
    if provinsi:
        # Mengelompokkan data pemeluk di provinsi tersebut berdasarkan agama
        data = filter(lambda item: item['provinsi'] == provinsi, data)
        
    # Mengelompokkan data pemeluk berdasarkan agama
    data = groupby(data, key=lambda item: item['agama'])

    # Menghitung jumlah pemeluk per agama
    agama_data = {agama: sum(item['jumlah_pemeluk'] for item in items) for agama, items in data}
    return agama_data

# Fungsi untuk menampilkan data provinsi
def tampilkan_data_provinsi(data):

    # Menampilkan daftar provinsi
    provinsi_data = group_by_provinsi(data)
    for i, (provinsi, _) in enumerate(provinsi_data.items(), start=1):
        st.write(f'[{i}] Provinsi {provinsi}')
   

# Fungsi untuk menampilkan jumlah pemeluk jumlah_pemeluk agama di Indonesia
def tampilkan_jumlah_pemeluk_agama(data):

    # Mengelompokkan data pemeluk berdasarkan agama
    agama_data = group_by_agama(data)

    # Menampilkan data agama
    for agama, jumlah_pemeluk in agama_data.items():
        st.write(f'Jumlah Pemeluk Agama {agama}: {jumlah_pemeluk} jiwa')

# Fungsi untuk menampilkan total pemeluk di suatu provinsi
def tampilkan_total_pemeluk_provinsi(provinsi, data):

    # Mengelompokkan data pemeluk berdasarkan agama di provinsi tersebut
    agama_data = group_by_agama(data, provinsi=provinsi)

# Fungsi untuk menampilkan data agama di suatu provinsi
def tampilkan_data_agama_provinsi(provinsi, data):

    st.title(f'DATA PEMELUK AGAMA PROVINSI {provinsi}')
    st.empty()

    # Mengelompokkan data pemeluk berdasarkan agama di provinsi tersebut
    agama_data = group_by_agama(data, provinsi=provinsi)
    for agama, jumlah_pemeluk in agama_data.items():

        st.write(f'  Pemeluk Agama {agama} : {jumlah_pemeluk}')
    st.empty()    
    st.empty()

# Fungsi untuk menampilkan total jumlah jumlah_pemeluk agama di Indonesia
def tampilkan_total_pemeluk(data):
    total_pemeluk = sum(item['jumlah_pemeluk'] for item in data)
    st.info(f'TOTAL PEMELUK AGAMA INDONESIA : {total_pemeluk} JIWA')

# Program utama
if __name__ == '__main__':
    while True:
        # Menampilkan menu utama
        st.title('PENCARIAN DATA AGAMA INDONESIA TAHUN 2021')
        st.write('[1] Data Provinsi Agama di Indonesia ')
        st.write('[2] Total Pemeluk Agama        ')   
        st.write('[3] Exit                       ')
        pilihan = st.number_input('Masukan angka pilihan yang tersedia : ',min_value=1)

        if pilihan == 1:
            # Menampilkan data provinsi di Indonesia
            st.snow()
            st.title ("DATA PROVINSI AGAMA DI INDONESIA")
            tampilkan_data_provinsi(data)
            

            # Meminta input pilihan provinsi 
            pilihan_provinsi = st.number_input('Masukkan Pilihan Provinsi Yang Tersedia: ',min_value=1)
            if pilihan_provinsi == 34:
                continue

            # Menyimpan nama provinsi yang dipilih
            if pilihan_provinsi == (1,34):
                continue

            # Mencari nama provinsi sesuai dengan pilihan
            provinsi_data = group_by_provinsi(data)
            nama_provinsi = list(provinsi_data.keys())[int(pilihan_provinsi) -1]

            # Menampilkan data agama di provinsi tersebut
            st.title('Data Pemeluk Agama di Provinsi ' + nama_provinsi)
            agama_data = group_by_agama(data, provinsi=nama_provinsi)
            df = pd.DataFrame(list(agama_data.items()), columns=['Agama', 'Jumlah pemeluk'])
            st.table(df)

            # Meminta input untuk kembali ke menu utama
            break
        elif pilihan == 2:

            # Menampilkan total jumlah pemeluk di Indonesia
            tampilkan_total_pemeluk(data)

            # Meminta input untuk kembali ke menu utama
      
            break
        elif pilihan == 3:
            st.success('TERIMA KASIH!', icon="😁")
            st.empty()
            st.balloons()
            break
        else:
            st.error('Pilihan anda tidak valid!', icon="🚨")

#Menu Navbar
def main():
    st.sidebar.title("Menu Navigasi")
    menu = ["Data Agama per Provinsi"]
    choice = st.sidebar.selectbox(" ", menu)

    if choice == "Data Agama per Provinsi":
        provinsi = st.sidebar.selectbox("Masukkan Pilihan Provinsi Yang Tersedia:", list(group_by_provinsi(data).keys()))
        tampilkan_data_agama_provinsi(provinsi, data)
if __name__ == '__main__':
    main()



            



