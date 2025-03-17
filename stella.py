#! /usr/bin/env python
from __future__ import print_function

import sys
import argparse
from argparse import RawTextHelpFormatter
from leaderboard.utils.statistics_manager_local import StatisticsManager, FAILURE_MESSAGES
import pathlib
from carla_garage.leaderboard.leaderboard.leaderboard_evaluator_local import LeaderboardEvaluator

def run(args):

    pathlib.Path(args.checkpoint).parent.mkdir(parents=True, exist_ok=True)

    statistics_manager = StatisticsManager(args.checkpoint, args.debug_checkpoint)
    leaderboard_evaluator = LeaderboardEvaluator(args, statistics_manager)
    
    crashed = leaderboard_evaluator.run(args)

    del leaderboard_evaluator

    if crashed:
        sys.exit(-1)
    else:
        sys.exit(0)


def main():
    bool
    parser = argparse.ArgumentParser(description="stella", formatter_class=RawTextHelpFormatter)
    parser.add_argument('--host', default='localhost',
                        help='IP of the host server (default: localhost)')
    parser.add_argument('--port', default=2000, type=int,
                        help='TCP port to listen to (default: 2000)')
    parser.add_argument('--traffic-manager-port', default=8000, type=int,
                        help='Port to use for the TrafficManager (default: 8000)')
    parser.add_argument('--traffic-manager-seed', default=100, type=int,
                        help='Seed used by the TrafficManager (default: 100)')
    parser.add_argument('--debug', type=int,
                        help='Run with debug output', default=0)
    parser.add_argument('--record', type=str, default='',
                        help='Use CARLA recording feature to create a recording of the scenario')
    parser.add_argument('--timeout', default=300.0, type=float,
                        help='Set the CARLA client timeout value in seconds')

    # simulation setup
    parser.add_argument('--routes', required=True,
                        help='Name of the routes file to be executed.')
    parser.add_argument('--routes-subset', default='', type=str,
                        help='Execute a specific set of routes')
    parser.add_argument('--repetitions', type=int, default=1,
                        help='Number of repetitions per route.')

    # agent-related options
    parser.add_argument("-a", "--agent", type=str,
                        help="Path to Agent's py file to evaluate", required=True)
    parser.add_argument("--agent-config", type=str,
                        help="Path to Agent's configuration file", default="")

    parser.add_argument("--track", type=str, default='SENSORS',
                        help="Participation track: SENSORS, MAP")
    parser.add_argument('--resume', type=int, default=False,
                        help='Resume execution from last checkpoint?')
    parser.add_argument("--checkpoint", type=str, default='./simulation_results.json',
                        help="Path to checkpoint used for saving statistics and resuming")
    parser.add_argument("--debug-checkpoint", type=str, default='./live_results.txt',
                        help="Path to checkpoint used for saving live results")


    args = parser.parse_args()

    print(f"Connecting to CARLA at {args.host}:{args.port}")

    run(args)

if __name__=="__main__":
    main()


