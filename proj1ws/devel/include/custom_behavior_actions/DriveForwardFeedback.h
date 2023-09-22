// Generated by gencpp from file custom_behavior_actions/DriveForwardFeedback.msg
// DO NOT EDIT!


#ifndef CUSTOM_BEHAVIOR_ACTIONS_MESSAGE_DRIVEFORWARDFEEDBACK_H
#define CUSTOM_BEHAVIOR_ACTIONS_MESSAGE_DRIVEFORWARDFEEDBACK_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace custom_behavior_actions
{
template <class ContainerAllocator>
struct DriveForwardFeedback_
{
  typedef DriveForwardFeedback_<ContainerAllocator> Type;

  DriveForwardFeedback_()
    : progress(0.0)  {
    }
  DriveForwardFeedback_(const ContainerAllocator& _alloc)
    : progress(0.0)  {
  (void)_alloc;
    }



   typedef float _progress_type;
  _progress_type progress;





  typedef boost::shared_ptr< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct DriveForwardFeedback_

typedef ::custom_behavior_actions::DriveForwardFeedback_<std::allocator<void> > DriveForwardFeedback;

typedef boost::shared_ptr< ::custom_behavior_actions::DriveForwardFeedback > DriveForwardFeedbackPtr;
typedef boost::shared_ptr< ::custom_behavior_actions::DriveForwardFeedback const> DriveForwardFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator1> & lhs, const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.progress == rhs.progress;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator1> & lhs, const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace custom_behavior_actions

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "70805092fd20e110765c7b79e8efb737";
  }

  static const char* value(const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x70805092fd20e110ULL;
  static const uint64_t static_value2 = 0x765c7b79e8efb737ULL;
};

template<class ContainerAllocator>
struct DataType< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "custom_behavior_actions/DriveForwardFeedback";
  }

  static const char* value(const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#feedback\n"
"float32 progress\n"
;
  }

  static const char* value(const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.progress);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct DriveForwardFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::custom_behavior_actions::DriveForwardFeedback_<ContainerAllocator>& v)
  {
    s << indent << "progress: ";
    Printer<float>::stream(s, indent + "  ", v.progress);
  }
};

} // namespace message_operations
} // namespace ros

#endif // CUSTOM_BEHAVIOR_ACTIONS_MESSAGE_DRIVEFORWARDFEEDBACK_H
