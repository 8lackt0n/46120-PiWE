'''blah blah'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yaml


class GeneralWindTurbine():
    '''defines the specs for a wind turbine, 
    and has a generalist power curve function'''
    def __init__(self, rotor_diameter, hub_height,
                 rated_power, v_in, v_rated, v_out, name=None):
        self.rotor_diameter = rotor_diameter
        self.hub_height = hub_height
        self.rated_power = rated_power
        self.v_in = v_in
        self.v_rated = v_rated
        self.v_out = v_out
        self.name = name

    def get_power(self, speed):
        '''calculates the power based on the specs'''

        P = np.zeros(len(speed))

        for i, v in enumerate(speed):
            if self.v_in <= v and v < self.v_rated:
                P[i] = self.rated_power * (v / self.v_rated)**3
            elif self.v_rated <= v and v <= self.v_out:
                P[i] = self.rated_power
            else:
                P[i] = 0

        return P


class WindTurbine(GeneralWindTurbine):
    '''contains a specific power curve for a turbine, 
    and returns an interpolated version'''
    def __init__(self, power_curve_data, rotor_diameter, hub_height,
                 rated_power, v_in, v_rated, v_out, name=None):

        super().__init__(rotor_diameter, hub_height, rated_power, v_in,
                         v_rated, v_out, name)
        self.power_curve_data = power_curve_data

    def get_power(self, speed):
        '''get power based on interpolted curve'''
        v_data = self.power_curve_data['Wind Speed [m/s]']
        p_data = self.power_curve_data['Power [kW]']

        P = np.zeros(len(speed))
        for i, v in enumerate(speed):
            if v < self.v_in or v > self.v_out:
                P[i] = 0
            else:
                P[i] = np.interp(v, v_data, p_data)

        return P


def read_specs(path):
    '''reads the specs'''
    with open(path) as stream:
        data_loaded = yaml.safe_load(stream)

    rotor_diameter = data_loaded['rotor_diameter']
    hub_height = data_loaded['hub_height']
    rated_power = data_loaded['rated_power']
    v_in = data_loaded['cut_in_wind_speed']
    v_rated = data_loaded['rated_wind_speed']
    v_out = data_loaded['cut_out_wind_speed']

    return rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out


def read_power_curve(path):
    '''reads the power curve data'''
    df = pd.read_csv(path)

    data = df[['Wind Speed [m/s]', 'Power [kW]']]
    return data


if __name__ == "__main__":
    SPEC_PATH = r'week09_classes_inheritance_and_OOP\LEANWIND_specs.yaml'
    CURVE_PATH = r'week09_classes_inheritance_and_OOP\LEANWIND_speed_power.csv'

    rotor_diameter, hub_height, rated_power, v_in, v_rated, v_out = read_specs(SPEC_PATH)
    power_curve = read_power_curve(CURVE_PATH)

    gen_wind = GeneralWindTurbine(rotor_diameter, hub_height, rated_power,
                                  v_in, v_rated, v_out, 'GENERAL')
    spec_wind = WindTurbine(power_curve, rotor_diameter, hub_height,
                            rated_power, v_in, v_rated, v_out, 'SPECIFIC')

    speed_range = np.arange(0, 30, 0.1)
    gen_P = gen_wind.get_power(speed_range)
    spec_P = spec_wind.get_power(speed_range)

    plt.plot(speed_range, gen_P, label="GENERAL")
    plt.plot(speed_range, spec_P, label="SPECIFIC")
    plt.legend()
    plt.show()
