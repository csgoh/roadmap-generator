import pytest

# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.roadmapper.roadmap import Roadmap
from src.roadmapper.timelinemode import TimelineMode


@pytest.mark.unit
def test_defect_106():
    roadmap = Roadmap(1800, 400, colour_theme="BLUEMOUNTAIN")
    roadmap.set_title("My Demo Roadmap")
    roadmap.set_subtitle("Matariki Technologies Ltd")

    roadmap.set_timeline(
        TimelineMode.WEEKLY,
        start="2024-12-01",
        number_of_items=24,
        show_first_day_of_week=True,
    )
    # roadmap.set_timeline(TimelineMode.WEEKLY, start="2024-12-01", number_of_items=24)
    # roadmap.set_timeline(
    #     TimelineMode.MONTHLY,
    #     start="2024-12-01",
    #     number_of_items=24,
    #     show_first_day_of_week=True,
    # )

    group = roadmap.add_group("Core Product Work Stream")

    group.add_task("Base Functionality", "2024-12-01", "2025-01-05")
    group.add_task("Enhancements", "2025-01-06", "2025-03-31")

    roadmap.set_footer("Generated by Roadmapper")
    roadmap.draw()
    roadmap.save("../../images/defects/issue-106.png")
